from __future__ import annotations

import asyncio
import base64
import json
from pathlib import Path
from urllib.parse import parse_qs
from uuid import UUID

import httpx
import pytest

from ramp.client import AsyncRamp, Ramp
from ramp.errors import APIStatusError, AuthenticationError


def test_client_credentials_authenticate_and_send_request() -> None:
    requests: list[httpx.Request] = []

    def handle_request(request: httpx.Request) -> httpx.Response:
        requests.append(request)
        if request.url.path == "/developer/v1/token":
            expected_credentials = base64.b64encode(b"client-id:client-secret").decode()
            assert request.headers["Authorization"] == f"Basic {expected_credentials}"
            assert parse_qs(request.content.decode()) == {
                "grant_type": ["client_credentials"]
            }
            return httpx.Response(
                200,
                json={
                    "access_token": "access-token",
                    "expires_in": 604800,
                    "token_type": "Bearer",
                },
            )

        assert request.url == httpx.URL(
            "https://api.ramp.com/developer/v1/agent-tools/get-agent-card-funds"
        )
        assert request.headers["Authorization"] == "Bearer access-token"
        assert json.loads(request.read())["rationale"] in {
            "Verify the generated SDK can authenticate",
            "Verify the SDK reuses its access token",
        }
        return httpx.Response(200, json={"funds": []})

    http_client = httpx.Client(transport=httpx.MockTransport(handle_request))
    client = Ramp(
        client_id="client-id",
        client_secret="client-secret",
        environment="production",
        http_client=http_client,
    )

    result = client.agent_tools.agent_cards.list_funds(
        rationale="Verify the generated SDK can authenticate"
    )
    second_result = client.agent_tools.agent_cards.list_funds(
        rationale="Verify the SDK reuses its access token"
    )

    assert result == {"funds": []}
    assert second_result == {"funds": []}
    assert [request.url.path for request in requests] == [
        "/developer/v1/token",
        "/developer/v1/agent-tools/get-agent-card-funds",
        "/developer/v1/agent-tools/get-agent-card-funds",
    ]


def test_from_env_uses_client_credentials_without_legacy_wallet_key(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.setenv("RAMP_CLIENT_ID", "client-id")
    monkeypatch.setenv("RAMP_CLIENT_SECRET", "client-secret")
    monkeypatch.setenv("RAMP_AGENT_WALLET_API_KEY", "legacy-wallet-key")
    requests: list[httpx.Request] = []

    def handle_request(request: httpx.Request) -> httpx.Response:
        requests.append(request)
        assert "legacy-wallet-key" not in str(request.headers)
        assert b"legacy-wallet-key" not in request.content
        if request.url.path == "/developer/v1/token":
            return httpx.Response(
                200,
                json={"access_token": "access-token", "expires_in": 604800},
            )
        return httpx.Response(200, json={"funds": []})

    client = Ramp.from_env(
        environment="production",
        http_client=httpx.Client(transport=httpx.MockTransport(handle_request)),
    )

    assert client.agent_tools.agent_cards.list_funds(
        rationale="Authenticate from environment variables"
    ) == {"funds": []}
    assert [request.url.path for request in requests] == [
        "/developer/v1/token",
        "/developer/v1/agent-tools/get-agent-card-funds",
    ]


def test_from_env_requires_both_client_credentials(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.setenv("RAMP_CLIENT_ID", "client-id")
    monkeypatch.delenv("RAMP_CLIENT_SECRET", raising=False)

    with pytest.raises(ValueError, match="RAMP_CLIENT_SECRET"):
        Ramp.from_env(environment="production")


def test_partial_client_credentials_are_rejected_with_an_access_token() -> None:
    with pytest.raises(
        TypeError,
        match="client_id and client_secret must be provided together",
    ):
        Ramp(
            client_id="client-id",
            access_token="access-token",
            environment="production",
        )


def test_access_token_skips_client_credentials_exchange() -> None:
    requests: list[httpx.Request] = []

    def handle_request(request: httpx.Request) -> httpx.Response:
        requests.append(request)
        assert request.headers["Authorization"] == "Bearer supplied-token"
        return httpx.Response(200, json={"funds": []})

    client = Ramp(
        access_token="supplied-token",
        environment="production",
        http_client=httpx.Client(transport=httpx.MockTransport(handle_request)),
    )

    assert client.agent_tools.agent_cards.list_funds(
        rationale="Use a caller-supplied token"
    ) == {"funds": []}
    assert [request.url.path for request in requests] == [
        "/developer/v1/agent-tools/get-agent-card-funds"
    ]


def test_agent_card_payment_token_uses_vault_api() -> None:
    def handle_request(request: httpx.Request) -> httpx.Response:
        assert request.url == httpx.URL(
            "https://vault-api.ramp.com/developer/v1/agent-tools/get-agent-card-creds"
        )
        assert request.headers["Authorization"] == "Bearer supplied-token"
        assert request.headers["X-Idempotency-Key"] == "checkout-attempt-1"
        return httpx.Response(200, json={})

    client = Ramp(
        access_token="supplied-token",
        environment="sandbox",
        http_client=httpx.Client(transport=httpx.MockTransport(handle_request)),
    )

    assert (
        client.agent_tools.agent_cards.create_payment_token(
            amount="45.00",
            currency_code="USD",
            fund_id="fund-uuid",
            idempotency_key="checkout-attempt-1",
            merchant_country_code="US",
            merchant_name="Figma Inc",
            merchant_url="https://figma.com",
            rationale="Create a token for the approved checkout",
        )
        == {}
    )


def test_async_client_credentials_authenticate_and_send_request() -> None:
    requests: list[httpx.Request] = []

    def handle_request(request: httpx.Request) -> httpx.Response:
        requests.append(request)
        if request.url.path == "/developer/v1/token":
            return httpx.Response(
                200,
                json={"access_token": "async-token", "expires_in": 604800},
            )
        assert request.headers["Authorization"] == "Bearer async-token"
        return httpx.Response(200, json={"funds": []})

    async def run() -> dict[str, object]:
        client = AsyncRamp(
            client_id="client-id",
            client_secret="client-secret",
            environment="production",
            http_client=httpx.AsyncClient(
                transport=httpx.MockTransport(handle_request)
            ),
        )
        return await client.agent_tools.agent_cards.list_funds(
            rationale="Verify async authentication"
        )

    assert asyncio.run(run()) == {"funds": []}
    assert [request.url.path for request in requests] == [
        "/developer/v1/token",
        "/developer/v1/agent-tools/get-agent-card-funds",
    ]


def test_async_agent_card_payment_token_uses_vault_api() -> None:
    def handle_request(request: httpx.Request) -> httpx.Response:
        assert request.url == httpx.URL(
            "https://vault-api.ramp.com/developer/v1/agent-tools/get-agent-card-creds"
        )
        assert request.headers["Authorization"] == "Bearer supplied-token"
        assert request.headers["X-Idempotency-Key"] == "checkout-attempt-1"
        return httpx.Response(200, json={})

    async def run() -> dict[str, object]:
        client = AsyncRamp(
            access_token="supplied-token",
            environment="production",
            http_client=httpx.AsyncClient(
                transport=httpx.MockTransport(handle_request)
            ),
        )
        return await client.agent_tools.agent_cards.create_payment_token(
            amount="45.00",
            currency_code="USD",
            fund_id="fund-uuid",
            idempotency_key="checkout-attempt-1",
            merchant_country_code="US",
            merchant_name="Figma Inc",
            merchant_url="https://figma.com",
            rationale="Create a token for the approved checkout",
        )

    assert asyncio.run(run()) == {}


def test_async_from_env_uses_client_credentials(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.setenv("RAMP_CLIENT_ID", "client-id")
    monkeypatch.setenv("RAMP_CLIENT_SECRET", "client-secret")

    def handle_request(request: httpx.Request) -> httpx.Response:
        if request.url.path == "/developer/v1/token":
            return httpx.Response(
                200,
                json={"access_token": "access-token", "expires_in": 604800},
            )
        return httpx.Response(200, json={"funds": []})

    async def run() -> dict[str, object]:
        client = AsyncRamp.from_env(
            environment="production",
            http_client=httpx.AsyncClient(
                transport=httpx.MockTransport(handle_request)
            ),
        )
        return await client.agent_tools.agent_cards.list_funds(
            rationale="Verify async environment authentication"
        )

    assert asyncio.run(run()) == {"funds": []}


def test_runtime_serializes_path_and_uuid_body_values() -> None:
    def handle_request(request: httpx.Request) -> httpx.Response:
        assert request.url.path == (
            "/developer/v1/agent-wallet/agents/agent-id/policies"
        )
        assert json.loads(request.content) == {
            "configurations": [{"configuration_id": "vic-usd", "method": "vic"}],
            "constraints": {"currency": "USD", "max_amount": "100.00"},
            "policy_version": "c449f728-36d2-4db1-b607-d2a987b5e43e",
            "schema_version": 1,
        }
        return httpx.Response(204)

    client = Ramp(
        access_token="supplied-token",
        environment="production",
        http_client=httpx.Client(transport=httpx.MockTransport(handle_request)),
    )

    assert (
        client.agent_wallet.publish_policy(
            agent_id="agent-id",
            configurations=[{"configuration_id": "vic-usd", "method": "vic"}],
            constraints={"currency": "USD", "max_amount": "100.00"},
            policy_version=UUID("c449f728-36d2-4db1-b607-d2a987b5e43e"),
            schema_version=1,
        )
        is None
    )


def test_invalid_client_credentials_raise_authentication_error() -> None:
    def handle_request(request: httpx.Request) -> httpx.Response:
        assert request.url.path == "/developer/v1/token"
        return httpx.Response(
            401,
            json={
                "error": "invalid_client",
                "error_description": "Client credentials are invalid.",
            },
        )

    client = Ramp(
        client_id="invalid-client",
        client_secret="invalid-secret",
        environment="production",
        http_client=httpx.Client(transport=httpx.MockTransport(handle_request)),
    )

    with pytest.raises(AuthenticationError) as error:
        client.agent_tools.agent_cards.list_funds(
            rationale="Verify invalid credentials are classified"
        )

    assert error.value.status_code == 401
    assert str(error.value) == "Client credentials are invalid."


def test_transient_token_failure_raises_api_status_error() -> None:
    def handle_request(request: httpx.Request) -> httpx.Response:
        assert request.url.path == "/developer/v1/token"
        return httpx.Response(503, json={"message": "Temporarily unavailable."})

    client = Ramp(
        client_id="client-id",
        client_secret="client-secret",
        environment="production",
        http_client=httpx.Client(transport=httpx.MockTransport(handle_request)),
    )

    with pytest.raises(APIStatusError) as error:
        client.agent_tools.agent_cards.list_funds(
            rationale="Verify transient token errors are classified"
        )

    assert not isinstance(error.value, AuthenticationError)
    assert error.value.status_code == 503
    assert str(error.value) == "Temporarily unavailable."


def test_close_only_closes_an_owned_http_client(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    owned_http_client = httpx.Client(transport=httpx.MockTransport(lambda _: None))
    supplied_http_client = httpx.Client(transport=httpx.MockTransport(lambda _: None))
    monkeypatch.setattr(httpx, "Client", lambda **_: owned_http_client)
    owned_client = Ramp(access_token="supplied-token", environment="production")
    supplied_client = Ramp(
        access_token="supplied-token",
        environment="production",
        http_client=supplied_http_client,
    )

    owned_client.close()
    supplied_client.close()

    assert owned_http_client.is_closed
    assert not supplied_http_client.is_closed
    supplied_http_client.close()


def test_aclose_only_closes_an_owned_async_http_client(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    async def run() -> tuple[bool, bool]:
        owned_http_client = httpx.AsyncClient(
            transport=httpx.MockTransport(lambda _: None)
        )
        supplied_http_client = httpx.AsyncClient(
            transport=httpx.MockTransport(lambda _: None)
        )
        monkeypatch.setattr(httpx, "AsyncClient", lambda **_: owned_http_client)
        owned_client = AsyncRamp(
            access_token="supplied-token", environment="production"
        )
        supplied_client = AsyncRamp(
            access_token="supplied-token",
            environment="production",
            http_client=supplied_http_client,
        )

        await owned_client.aclose()
        await supplied_client.aclose()
        supplied_is_closed = supplied_http_client.is_closed
        await supplied_http_client.aclose()
        return owned_http_client.is_closed, supplied_is_closed

    assert asyncio.run(run()) == (True, False)


def test_runtime_uploads_a_file_path_as_multipart(tmp_path: Path) -> None:
    upload = tmp_path / "quote.pdf"
    upload.write_bytes(b"vendor quote")

    def handle_request(request: httpx.Request) -> httpx.Response:
        assert request.url.path == ("/developer/v1/agent-tools/procurement-upload-file")
        content = request.read()
        assert b"vendor quote" in content
        assert b'name="file"; filename="quote.pdf"' in content
        assert b"9e1c8ff9-8a33-4e2a-970e-b984068f2f75" in content
        return httpx.Response(200, json={"file_id": "file-id"})

    client = Ramp(
        access_token="supplied-token",
        environment="production",
        http_client=httpx.Client(transport=httpx.MockTransport(handle_request)),
    )

    assert client.agent_tools.procurement_requests.upload_file(
        field_id="supporting-document",
        file=upload,
        rationale="Attach the vendor quote",
        spend_request_uuid=UUID("9e1c8ff9-8a33-4e2a-970e-b984068f2f75"),
    ) == {"file_id": "file-id"}
