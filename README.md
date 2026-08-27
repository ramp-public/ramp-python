# Ramp Python SDK

The official Python SDK for Ramp.

The SDK provides synchronous and asynchronous clients for Ramp's Developer API
and Agent Tools APIs. It uses the same OAuth scopes, roles, feature gates, and
authorization checks as direct API requests.

> **Release status:** the source is being prepared for its first public release.
> A PyPI package is not available yet.

## Requirements

- Python 3.11 or newer
- Ramp Developer API credentials

## Development setup

```bash
git clone https://github.com/ramp-public/ramp-python.git
cd ramp-python
uv sync --group test
```

## Authentication

The default environment is Ramp's sandbox. Set `RAMP_CLIENT_ID` and
`RAMP_CLIENT_SECRET`, then create a client from the environment:

```python
from ramp import Ramp


with Ramp.from_env() as client:
    funds = client.agent_tools.agent_cards.list_funds(
        rationale="Find eligible Agent Card funds",
    )
```

You can also provide credentials explicitly:

```python
from ramp import AsyncRamp


async with AsyncRamp(
    client_id="your-client-id",
    client_secret="your-client-secret",
    environment="sandbox",
) as client:
    funds = await client.agent_tools.agent_cards.list_funds(
        rationale="Find eligible Agent Card funds",
    )
```

Callers that already manage token acquisition can use `access_token=...`.
Select `environment="production"` only when using production credentials.

Standalone Agent credentials use the OAuth 2.0 client-credentials grant. A
generic Developer API client remains business-scoped; passing it to this SDK
does not turn it into a Standalone Agent. The SDK does not read or transmit the
legacy `RAMP_AGENT_WALLET_API_KEY` variable.

## Standalone Agent to Agent Card credential

This example uses two distinct identities:

1. The Ramp CLI uses a human, business-scoped profile to create the Standalone
   Agent.
2. The Python SDK uses the new agent's show-once credentials to act as that
   Standalone Agent.

First, create the agent with an existing custom role. The authorizing user must
be allowed to manage roles and Standalone Agents.

```bash
ramp --profile human agent create \
  --name "Procurement Agent" \
  --role-id 7c322160-2871-4382-b026-92597ce3ed19
```

Store the returned client ID and client secret immediately; the secret is shown
only once. Also retain the returned agent ID. Add that agent to the exact shared
fund it should use; this continues to use the existing fund-membership command:

```bash
ramp --profile human funds add-user \
  --spend-allocation-uuid "<approved-fund-id>" \
  --agent-id "<standalone-agent-id>" \
  --rationale "Give the procurement agent access to the approved fund"
```

The human profile must be allowed to edit the fund, and the agent must be active
and have permission to possess funds. Then export the agent credentials for the
SDK:

```bash
export RAMP_CLIENT_ID="<standalone-agent-client-id>"
export RAMP_CLIENT_SECRET="<standalone-agent-client-secret>"
```

Using those credentials, list the funds that are eligible for Agent Card
issuance, verify the exact fund and checkout details, and request one fresh
credential for one checkout:

```python
from uuid import uuid4

from ramp import Ramp


with Ramp.from_env(environment="sandbox") as agent:
    eligible_funds = agent.agent_tools.agent_cards.list_funds(
        rationale="Select the approved fund for the office-supplies checkout",
    )

    # Select and verify an exact fund from eligible_funds before issuance.
    fund_id = "<approved-fund-id>"

    payment_token = agent.agent_tools.agent_cards.create_payment_token(
        amount="45.00",
        currency_code="USD",
        fund_id=fund_id,
        idempotency_key=str(uuid4()),
        merchant_country_code="US",
        merchant_name="Example Office Supply",
        merchant_url="https://merchant.example",
        rationale="Issue one credential for the approved $45.00 checkout",
    )

    # Keep payment_token in memory and submit it once to the intended checkout.
    # Do not print, log, persist, or retry an ambiguous issuance.
```

`create_payment_token` calls the historical `get_agent_card_creds` operation,
but it is a one-time credential issuance rather than a read-only GET. A new
idempotency key is required for a new checkout attempt. Do not automatically
retry after an ambiguous response.

## Safety and permissions

The generated client includes read, write, destructive, and feature-gated
operations. Availability in the SDK does not grant permission to call an
operation. Ramp still enforces OAuth scopes, user or agent roles, feature gates,
and resource-level authorization.

Treat credential- and payment-token responses as secrets. Do not log them.
Avoid automatically retrying writes, destructive requests, or ambiguous
credential-issuance outcomes unless the operation has an idempotency contract.

## Development

```bash
uv run ruff check src tests
uv run ruff format --check src tests
uv run pytest
./scripts/verify_package.sh
```

The generated API surface lives in `src/ramp/_generated/agent_tools.py`. Do not
edit it by hand. See [CONTRIBUTING.md](CONTRIBUTING.md) for development and
release-boundary guidance.

## Security

Please do not report vulnerabilities in public GitHub issues. Follow Ramp's
[security reporting guidance](https://ramp.com/security).

## License

[MIT](LICENSE)
