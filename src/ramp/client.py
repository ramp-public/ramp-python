"""Public clients for Ramp's first-party Python SDK."""

from __future__ import annotations

import os
from typing import Self

import httpx

from ._generated.agent_tools import AsyncRamp as _GeneratedAsyncRamp
from ._generated.agent_tools import Ramp as _GeneratedRamp
from ._http import AsyncHttpxTransport, Environment, HttpxTransport
from ._types import AsyncTransport, SyncTransport

_CLIENT_ID_ENV_VAR = "RAMP_CLIENT_ID"
_CLIENT_SECRET_ENV_VAR = "RAMP_CLIENT_SECRET"


def _client_credentials_from_env() -> tuple[str, str]:
    client_id = os.environ.get(_CLIENT_ID_ENV_VAR)
    client_secret = os.environ.get(_CLIENT_SECRET_ENV_VAR)
    missing = [
        name
        for name, value in (
            (_CLIENT_ID_ENV_VAR, client_id),
            (_CLIENT_SECRET_ENV_VAR, client_secret),
        )
        if not value
    ]
    if missing:
        raise ValueError(
            f"missing required environment variable(s): {', '.join(missing)}"
        )
    assert client_id is not None and client_secret is not None
    return client_id, client_secret


def _has_client_credentials(
    *, client_id: str | None, client_secret: str | None
) -> bool:
    if not client_id or not client_secret:
        if client_id is not None or client_secret is not None:
            raise TypeError("client_id and client_secret must be provided together")
        return False
    return True


class Ramp(_GeneratedRamp):
    """Synchronous Ramp API client."""

    def __init__(
        self,
        *,
        client_id: str | None = None,
        client_secret: str | None = None,
        access_token: str | None = None,
        environment: Environment = "sandbox",
        http_client: httpx.Client | None = None,
        transport: SyncTransport | None = None,
    ) -> None:
        if transport is not None:
            if any(
                value is not None
                for value in (client_id, client_secret, access_token, http_client)
            ):
                raise TypeError(
                    "transport cannot be combined with client credentials or http_client"
                )
            resolved_transport = transport
        else:
            has_credentials = _has_client_credentials(
                client_id=client_id,
                client_secret=client_secret,
            )
            if access_token and has_credentials:
                raise TypeError(
                    "access_token cannot be combined with client credentials"
                )
            if not access_token and not has_credentials:
                raise TypeError(
                    "provide access_token or both client_id and client_secret"
                )
            resolved_transport = HttpxTransport(
                client_id=client_id,
                client_secret=client_secret,
                access_token=access_token,
                environment=environment,
                http_client=http_client,
            )
        self._runtime_transport = (
            resolved_transport
            if isinstance(resolved_transport, HttpxTransport)
            else None
        )
        super().__init__(transport=resolved_transport)

    @classmethod
    def from_env(
        cls,
        *,
        environment: Environment = "sandbox",
        http_client: httpx.Client | None = None,
    ) -> Self:
        """Create a client from client credentials in the environment."""
        client_id, client_secret = _client_credentials_from_env()
        return cls(
            client_id=client_id,
            client_secret=client_secret,
            environment=environment,
            http_client=http_client,
        )

    def close(self) -> None:
        """Close resources owned by this client."""
        if self._runtime_transport is not None:
            self._runtime_transport.close()

    def __enter__(self) -> Ramp:
        return self

    def __exit__(self, *args: object) -> None:
        self.close()


class AsyncRamp(_GeneratedAsyncRamp):
    """Asynchronous Ramp API client."""

    def __init__(
        self,
        *,
        client_id: str | None = None,
        client_secret: str | None = None,
        access_token: str | None = None,
        environment: Environment = "sandbox",
        http_client: httpx.AsyncClient | None = None,
        transport: AsyncTransport | None = None,
    ) -> None:
        if transport is not None:
            if any(
                value is not None
                for value in (client_id, client_secret, access_token, http_client)
            ):
                raise TypeError(
                    "transport cannot be combined with client credentials or http_client"
                )
            resolved_transport = transport
        else:
            has_credentials = _has_client_credentials(
                client_id=client_id,
                client_secret=client_secret,
            )
            if access_token and has_credentials:
                raise TypeError(
                    "access_token cannot be combined with client credentials"
                )
            if not access_token and not has_credentials:
                raise TypeError(
                    "provide access_token or both client_id and client_secret"
                )
            resolved_transport = AsyncHttpxTransport(
                client_id=client_id,
                client_secret=client_secret,
                access_token=access_token,
                environment=environment,
                http_client=http_client,
            )
        self._runtime_transport = (
            resolved_transport
            if isinstance(resolved_transport, AsyncHttpxTransport)
            else None
        )
        super().__init__(transport=resolved_transport)

    @classmethod
    def from_env(
        cls,
        *,
        environment: Environment = "sandbox",
        http_client: httpx.AsyncClient | None = None,
    ) -> Self:
        """Create a client from client credentials in the environment."""
        client_id, client_secret = _client_credentials_from_env()
        return cls(
            client_id=client_id,
            client_secret=client_secret,
            environment=environment,
            http_client=http_client,
        )

    async def aclose(self) -> None:
        """Close resources owned by this client."""
        if self._runtime_transport is not None:
            await self._runtime_transport.aclose()

    async def __aenter__(self) -> AsyncRamp:
        return self

    async def __aexit__(self, *args: object) -> None:
        await self.aclose()


__all__ = ["AsyncRamp", "Ramp"]
