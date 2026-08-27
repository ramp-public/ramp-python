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

    sync_agents = Ramp(transport=RecordingSyncTransport()).agents
    async_agents = AsyncRamp(transport=RecordingAsyncTransport()).agents
    for method_name in (
        "create",
        "delete",
        "get",
        "list",
        "rotate_secret",
        "set_status",
        "update",
    ):
        assert inspect.signature(
            getattr(sync_agents, method_name)
        ) == inspect.signature(getattr(async_agents, method_name))


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


def test_add_user_to_shared_fund_accepts_standalone_agent_id() -> None:
    transport = RecordingSyncTransport()
    client = Ramp(transport=transport)
    agent_id = UUID("00000000-0000-4000-8000-000000000002")

    client.agent_tools.funds.add_user(
        agent_id=agent_id,
        rationale="Give the purchasing agent access to the approved fund",
        spend_allocation_uuid="00000000-0000-4000-8000-000000000001",
    )

    assert transport.calls[0] == {
        "method": "POST",
        "path": "/developer/v1/agent-tools/add-user-to-shared-fund",
        "path_params": None,
        "params": None,
        "headers": None,
        "json": {
            "agent_id": agent_id,
            "rationale": "Give the purchasing agent access to the approved fund",
            "spend_allocation_uuid": "00000000-0000-4000-8000-000000000001",
        },
        "data": None,
        "files": None,
        "metadata": OPERATION_METADATA["agent_tools.funds.add_user"],
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


def test_standalone_agent_lifecycle_uses_developer_api_contract() -> None:
    transport = RecordingSyncTransport()
    client = Ramp(transport=transport)
    agent_id = UUID("8a2c7f2e-5f5e-4f5a-9e2f-2c1c0b9b1a11")
    role_id = UUID("7c322160-2871-4382-b026-92597ce3ed19")

    assert client.agents.create(
        name="Procurement Agent",
        description="Automates approved office-supply purchases",
        role_ids=[role_id],
    ) == {"ok": True}
    assert client.agents.get(agent_id=agent_id) == {"ok": True}
    assert client.agents.update(
        agent_id=agent_id,
        description=None,
        name="Office Supply Agent",
    ) == {"ok": True}
    assert client.agents.set_status(agent_id=agent_id, status="INACTIVE") is None
    assert client.agents.rotate_secret(agent_id=agent_id) == {"ok": True}
    assert client.agents.delete(agent_id=agent_id) is None

    assert transport.calls == [
        {
            "method": "POST",
            "path": "/developer/v1/agents",
            "path_params": None,
            "params": None,
            "headers": None,
            "json": {
                "description": "Automates approved office-supply purchases",
                "name": "Procurement Agent",
                "role_ids": [role_id],
            },
            "data": None,
            "files": None,
            "metadata": OPERATION_METADATA["agents.create"],
        },
        {
            "method": "GET",
            "path": "/developer/v1/agents/{agent_id}",
            "path_params": {"agent_id": agent_id},
            "params": None,
            "headers": None,
            "json": None,
            "data": None,
            "files": None,
            "metadata": OPERATION_METADATA["agents.get"],
        },
        {
            "method": "PATCH",
            "path": "/developer/v1/agents/{agent_id}",
            "path_params": {"agent_id": agent_id},
            "params": None,
            "headers": None,
            "json": {"description": None, "name": "Office Supply Agent"},
            "data": None,
            "files": None,
            "metadata": OPERATION_METADATA["agents.update"],
        },
        {
            "method": "POST",
            "path": "/developer/v1/agents/{agent_id}/status",
            "path_params": {"agent_id": agent_id},
            "params": None,
            "headers": None,
            "json": {"status": "INACTIVE"},
            "data": None,
            "files": None,
            "metadata": OPERATION_METADATA["agents.set_status"],
        },
        {
            "method": "POST",
            "path": "/developer/v1/agents/{agent_id}/secret",
            "path_params": {"agent_id": agent_id},
            "params": None,
            "headers": None,
            "json": None,
            "data": None,
            "files": None,
            "metadata": OPERATION_METADATA["agents.rotate_secret"],
        },
        {
            "method": "DELETE",
            "path": "/developer/v1/agents/{agent_id}",
            "path_params": {"agent_id": agent_id},
            "params": None,
            "headers": None,
            "json": None,
            "data": None,
            "files": None,
            "metadata": OPERATION_METADATA["agents.delete"],
        },
    ]


def test_async_client_awaits_async_transport() -> None:
    transport = RecordingAsyncTransport()
    client = AsyncRamp(transport=transport)

    result = asyncio.run(
        client.agent_tools.bills.list(rationale="Find bills awaiting payment")
    )

    assert result == {"ok": True}
    assert transport.calls[0]["json"] == {"rationale": "Find bills awaiting payment"}
