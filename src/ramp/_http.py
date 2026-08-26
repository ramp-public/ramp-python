"""Handwritten HTTP runtime for the generated Ramp resources."""

from __future__ import annotations

from collections.abc import Mapping, Sequence
from contextlib import ExitStack
from dataclasses import dataclass
from datetime import date, datetime
from decimal import Decimal
from enum import Enum
from os import PathLike, fspath
from pathlib import Path
from time import monotonic
from typing import Any, Literal
from uuid import UUID

import httpx

from ._types import FileInput, OperationMetadata
from .errors import APIStatusError, AuthenticationError

Environment = Literal["sandbox", "production"]

_BASE_URLS: dict[Environment, str] = {
    "sandbox": "https://demo-api.ramp.com",
    "production": "https://api.ramp.com",
}
_TOKEN_PATH = "/developer/v1/token"
_EXPIRY_SKEW_SECONDS = 30


def _jsonable(value: Any) -> Any:
    if value is None or isinstance(value, bool | int | float | str):
        return value
    if isinstance(value, Enum):
        return _jsonable(value.value)
    if isinstance(value, datetime | date):
        return value.isoformat()
    if isinstance(value, UUID | Decimal):
        return str(value)
    if isinstance(value, Mapping):
        return {str(key): _jsonable(child) for key, child in value.items()}
    if isinstance(value, Sequence) and not isinstance(value, bytes | bytearray):
        return [_jsonable(child) for child in value]
    raise TypeError(f"unsupported JSON value: {type(value).__name__}")


def _form_data(values: dict[str, Any] | None) -> dict[str, Any] | None:
    if values is None:
        return None
    return {key: _jsonable(value) for key, value in values.items()}


def _multipart_files(
    values: dict[str, FileInput] | None,
    stack: ExitStack,
) -> dict[str, Any] | None:
    if values is None:
        return None
    prepared: dict[str, Any] = {}
    for key, value in values.items():
        if isinstance(value, PathLike):
            file = stack.enter_context(open(value, "rb"))
            prepared[key] = (Path(fspath(value)).name, file)
        else:
            prepared[key] = value
    return prepared


def _error_message(response: httpx.Response) -> str:
    try:
        payload = response.json()
    except ValueError:
        return response.text.strip() or f"HTTP {response.status_code}"
    if isinstance(payload, Mapping):
        for container in (payload, payload.get("error"), payload.get("error_v2")):
            if not isinstance(container, Mapping):
                continue
            for key in ("error_description", "message"):
                message = container.get(key)
                if isinstance(message, str) and message:
                    return message
    return f"HTTP {response.status_code}"


def _raise_for_status(response: httpx.Response, *, authentication: bool) -> None:
    if not response.is_error:
        return
    error_type = AuthenticationError if authentication else APIStatusError
    raise error_type(
        _error_message(response),
        status_code=response.status_code,
    )


@dataclass(frozen=True, slots=True)
class _AccessToken:
    value: str
    expires_at: float


class HttpxTransport:
    """Authenticate and execute synchronous generated SDK requests."""

    def __init__(
        self,
        *,
        client_id: str | None,
        client_secret: str | None,
        access_token: str | None,
        environment: Environment,
        http_client: httpx.Client | None = None,
    ) -> None:
        self._client_id = client_id
        self._client_secret = client_secret
        self._base_url = _BASE_URLS[environment]
        self._owns_client = http_client is None
        self._client = http_client or httpx.Client(timeout=30)
        self._access_token = (
            _AccessToken(value=access_token, expires_at=float("inf"))
            if access_token is not None
            else None
        )

    def request(
        self,
        *,
        method: str,
        path: str,
        path_params: dict[str, Any] | None,
        params: dict[str, Any] | None,
        headers: dict[str, Any] | None,
        json: dict[str, Any] | None,
        data: dict[str, Any] | None,
        files: dict[str, FileInput] | None,
        metadata: OperationMetadata,
    ) -> object:
        del metadata
        if path_params:
            path = path.format(
                **{key: str(value) for key, value in path_params.items()}
            )
        request_headers = {key: str(value) for key, value in (headers or {}).items()}
        request_headers["Authorization"] = f"Bearer {self._get_access_token()}"
        with ExitStack() as stack:
            response = self._client.request(
                method,
                f"{self._base_url}{path}",
                params=params,
                headers=request_headers,
                json=_jsonable(json),
                data=_form_data(data),
                files=_multipart_files(files, stack),
            )
        _raise_for_status(response, authentication=False)
        if response.status_code == 204 or not response.content:
            return None
        return response.json()

    def _get_access_token(self) -> str:
        if (
            self._access_token is not None
            and self._access_token.expires_at - _EXPIRY_SKEW_SECONDS > monotonic()
        ):
            return self._access_token.value

        response = self._client.post(
            f"{self._base_url}{_TOKEN_PATH}",
            data={"grant_type": "client_credentials"},
            auth=httpx.BasicAuth(
                self._client_id or "",
                self._client_secret or "",
            ),
        )
        _raise_for_status(
            response,
            authentication=response.status_code in {400, 401},
        )
        payload = response.json()
        access_token = payload.get("access_token")
        expires_in = payload.get("expires_in")
        if not isinstance(access_token, str) or not access_token:
            raise ValueError("token response did not include an access token")
        if isinstance(expires_in, bool) or not isinstance(expires_in, int):
            raise ValueError("token response did not include expires_in")
        self._access_token = _AccessToken(
            value=access_token,
            expires_at=monotonic() + expires_in,
        )
        return access_token

    def close(self) -> None:
        """Close the HTTP client when this transport created it."""
        if self._owns_client:
            self._client.close()


class AsyncHttpxTransport:
    """Authenticate and execute asynchronous generated SDK requests."""

    def __init__(
        self,
        *,
        client_id: str | None,
        client_secret: str | None,
        access_token: str | None,
        environment: Environment,
        http_client: httpx.AsyncClient | None = None,
    ) -> None:
        self._client_id = client_id
        self._client_secret = client_secret
        self._base_url = _BASE_URLS[environment]
        self._owns_client = http_client is None
        self._client = http_client or httpx.AsyncClient(timeout=30)
        self._access_token = (
            _AccessToken(value=access_token, expires_at=float("inf"))
            if access_token is not None
            else None
        )

    async def request(
        self,
        *,
        method: str,
        path: str,
        path_params: dict[str, Any] | None,
        params: dict[str, Any] | None,
        headers: dict[str, Any] | None,
        json: dict[str, Any] | None,
        data: dict[str, Any] | None,
        files: dict[str, FileInput] | None,
        metadata: OperationMetadata,
    ) -> object:
        del metadata
        if path_params:
            path = path.format(
                **{key: str(value) for key, value in path_params.items()}
            )
        request_headers = {key: str(value) for key, value in (headers or {}).items()}
        request_headers["Authorization"] = f"Bearer {await self._get_access_token()}"
        with ExitStack() as stack:
            response = await self._client.request(
                method,
                f"{self._base_url}{path}",
                params=params,
                headers=request_headers,
                json=_jsonable(json),
                data=_form_data(data),
                files=_multipart_files(files, stack),
            )
        _raise_for_status(response, authentication=False)
        if response.status_code == 204 or not response.content:
            return None
        return response.json()

    async def _get_access_token(self) -> str:
        if (
            self._access_token is not None
            and self._access_token.expires_at - _EXPIRY_SKEW_SECONDS > monotonic()
        ):
            return self._access_token.value

        response = await self._client.post(
            f"{self._base_url}{_TOKEN_PATH}",
            data={"grant_type": "client_credentials"},
            auth=httpx.BasicAuth(
                self._client_id or "",
                self._client_secret or "",
            ),
        )
        _raise_for_status(
            response,
            authentication=response.status_code in {400, 401},
        )
        payload = response.json()
        access_token = payload.get("access_token")
        expires_in = payload.get("expires_in")
        if not isinstance(access_token, str) or not access_token:
            raise ValueError("token response did not include an access token")
        if isinstance(expires_in, bool) or not isinstance(expires_in, int):
            raise ValueError("token response did not include expires_in")
        self._access_token = _AccessToken(
            value=access_token,
            expires_at=monotonic() + expires_in,
        )
        return access_token

    async def aclose(self) -> None:
        """Close the HTTP client when this transport created it."""
        if self._owns_client:
            await self._client.aclose()
