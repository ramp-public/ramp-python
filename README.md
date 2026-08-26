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
