# Contributing

Thanks for contributing to `ramp-python`.

## Setup

```bash
uv sync --group test
uv run pytest
uv run ruff check src tests
uv run ruff format --check src tests
./scripts/verify_package.sh
```

Please add tests for behavior changes and keep pull requests focused.

## Generated code

Do not edit `src/ramp/_generated/agent_tools.py` by hand. Ramp generates that
module from its Developer API contract and reviews the resulting public API
surface before syncing it here.

Core-only generator inputs, internal packaging metadata, private CI settings,
and internal dependencies must not be added to this repository.

## Security

Do not include credentials, access tokens, customer data, or sensitive API
responses in issues, tests, examples, or pull requests. Report vulnerabilities
using the process in [SECURITY.md](SECURITY.md).
