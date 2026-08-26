from __future__ import annotations

import asyncio
import inspect
from typing import Any
from uuid import UUID

from ramp._generated.agent_tools import OPERATION_METADATA
from ramp._types import OperationMetadata
from ramp.client import AsyncRamp, Ramp


class RecordingSyncTransport:
    def __init__(self) -> None:
        self.calls: list[dict[str, Any]] = []

    def request(self, **kwargs: Any) -> object:
        self.calls.append(kwargs)
        return {"ok": True}


class RecordingAsyncTransport:
    def __init__(self) -> None:
        self.calls: list[dict[str, Any]] = []

    async def request(self, **kwargs: Any) -> object:
        self.calls.append(kwargs)
        return {"ok": True}


def test_sync_and_async_clients_have_matching_public_signatures() -> None:
    sync_signature = inspect.signature(
        Ramp(transport=RecordingSyncTransport()).agent_tools.bills.list
    )
    async_signature = inspect.signature(
        AsyncRamp(transport=RecordingAsyncTransport()).agent_tools.bills.list
    )

    assert sync_signature == async_signature

    sync_agents_signature = inspect.signature(
        Ramp(transport=RecordingSyncTransport()).agents.list
    )
    async_agents_signature = inspect.signature(
        AsyncRamp(transport=RecordingAsyncTransport()).agents.list
    )

    assert sync_agents_signature == async_agents_signature


def test_parameterless_operation_is_available_on_complete_surface() -> None:
    transport = RecordingSyncTransport()
    client = Ramp(transport=transport)

    result = client.applications.get()

    assert result == {"ok": True}
    assert transport.calls == [
        {
            "method": "GET",
            "path": "/developer/v1/applications",
            "path_params": None,
            "params": None,
            "headers": None,
            "json": None,
            "data": None,
            "files": None,
            "metadata": OPERATION_METADATA["applications.get"],
        }
    ]


def test_body_cursor_request_omits_not_given_but_preserves_null() -> None:
    transport = RecordingSyncTransport()
    client = Ramp(transport=transport)

    result = client.agent_tools.bills.list(
        rationale="Find bills awaiting payment",
        page_cursor=None,
    )

    assert result == {"ok": True}
    assert transport.calls == [
        {
            "method": "POST",
            "path": "/developer/v1/agent-tools/list-bills",
            "path_params": None,
            "params": None,
            "headers": None,
            "json": {
                "page_cursor": None,
                "rationale": "Find bills awaiting payment",
            },
            "data": None,
            "files": None,
            "metadata": OPERATION_METADATA["agent_tools.bills.list"],
        }
    ]


def test_multipart_request_partitions_form_fields_and_file() -> None:
    transport = RecordingSyncTransport()
    client = Ramp(transport=transport)
    request_id = UUID("9e1c8ff9-8a33-4e2a-970e-b984068f2f75")

    client.agent_tools.procurement_requests.upload_file(
        field_id="supporting-document",
        file=b"invoice",
        rationale="Attach the vendor quote",
        spend_request_uuid=request_id,
    )

    assert transport.calls[0] == {
        "method": "POST",
        "path": "/developer/v1/agent-tools/procurement-upload-file",
        "path_params": None,
        "params": None,
        "headers": None,
        "json": None,
        "data": {
            "field_id": "supporting-document",
            "rationale": "Attach the vendor quote",
            "spend_request_uuid": request_id,
        },
        "files": {"file": b"invoice"},
        "metadata": OPERATION_METADATA["agent_tools.procurement_requests.upload_file"],
    }


def test_destructive_and_gated_metadata_survives_generation() -> None:
    metadata = OPERATION_METADATA["agent_tools.funds.create"]

    assert metadata == OperationMetadata(
        operation_id="post_agent_tool_api___issue_one_off_funds",
        scopes=("funds:write",),
        platforms=("cli", "mcp"),
        stability="beta",
        pagination="none",
        safety="destructive",
        gate="agent_fund_creation",
    )


def test_wallet_and_identity_metadata_survives_generation() -> None:
    assert OPERATION_METADATA["agent_tools.agent_cards.enroll"] == OperationMetadata(
        operation_id="post_agent_tool_api___enroll_business_in_agent_cards",
        scopes=("cards:write",),
        platforms=("cli", "mcp"),
        stability="beta",
        pagination="none",
        safety="destructive",
        gate=None,
    )
    assert OPERATION_METADATA["agent_wallet.publish_policy"] == OperationMetadata(
        operation_id="post_agent_wallet_policy_publication_resource",
        scopes=("agent_wallet_policy:write",),
        platforms=("cli", "mcp"),
        stability="beta",
        pagination="none",
        safety="write",
        gate="agent_wallet_enabled",
    )
    assert OPERATION_METADATA["agents.list"] == OperationMetadata(
        operation_id="get_agent_list_resource",
        scopes=("agents:read",),
        platforms=("cli",),
        stability="beta",
        pagination="query_cursor",
        safety="read_only",
        gate="identity_standalone_agents",
    )


def test_agent_card_payment_token_partitions_idempotency_header() -> None:
    transport = RecordingSyncTransport()
    client = Ramp(transport=transport)

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

    assert transport.calls[0] == {
        "method": "POST",
        "path": "/developer/v1/agent-tools/get-agent-card-creds",
        "path_params": None,
        "params": None,
        "headers": {"X-Idempotency-Key": "checkout-attempt-1"},
        "json": {
            "amount": "45.00",
            "currency_code": "USD",
            "fund_id": "fund-uuid",
            "merchant_country_code": "US",
            "merchant_name": "Figma Inc",
            "merchant_url": "https://figma.com",
            "rationale": "Create a token for the approved checkout",
        },
        "data": None,
        "files": None,
        "metadata": OPERATION_METADATA["agent_tools.agent_cards.create_payment_token"],
    }


def test_agent_wallet_policy_partitions_path_and_body() -> None:
    transport = RecordingSyncTransport()
    client = Ramp(transport=transport)
    policy_version = UUID("c449f728-36d2-4db1-b607-d2a987b5e43e")
    configurations = [{"configuration_id": "vic-usd", "method": "vic"}]
    constraints = {
        "currency": "USD",
        "ends_at": "2026-09-01T00:00:00Z",
        "max_amount": "500.00",
        "max_amount_per_payment": "100.00",
        "max_payments": 10,
        "starts_at": "2026-08-01T00:00:00Z",
    }

    result = client.agent_wallet.publish_policy(
        agent_id="agent-uuid",
        configurations=configurations,
        constraints=constraints,
        policy_version=policy_version,
        schema_version=1,
    )

    assert result is None

    assert transport.calls[0] == {
        "method": "POST",
        "path": "/developer/v1/agent-wallet/agents/{agent_id}/policies",
        "path_params": {"agent_id": "agent-uuid"},
        "params": None,
        "headers": None,
        "json": {
            "configurations": configurations,
            "constraints": constraints,
            "policy_version": policy_version,
            "schema_version": 1,
        },
        "data": None,
        "files": None,
        "metadata": OPERATION_METADATA["agent_wallet.publish_policy"],
    }


def test_standalone_agent_list_uses_query_pagination() -> None:
    transport = RecordingSyncTransport()
    client = Ramp(transport=transport)

    client.agents.list(page_size=50, start="next-page")

    assert transport.calls[0] == {
        "method": "GET",
        "path": "/developer/v1/agents",
        "path_params": None,
        "params": {"page_size": 50, "start": "next-page"},
        "headers": None,
        "json": None,
        "data": None,
        "files": None,
        "metadata": OPERATION_METADATA["agents.list"],
    }


def test_async_client_awaits_async_transport() -> None:
    transport = RecordingAsyncTransport()
    client = AsyncRamp(transport=transport)

    result = asyncio.run(
        client.agent_tools.bills.list(rationale="Find bills awaiting payment")
    )

    assert result == {"ok": True}
    assert transport.calls[0]["json"] == {"rationale": "Find bills awaiting payment"}
