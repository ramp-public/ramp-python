#!/bin/bash

set -euo pipefail

if [ "$#" -ne 1 ]; then
    echo "Usage: $0 <wheel-path>"
    exit 1
fi

WHEEL_PATH="$(python -c 'from pathlib import Path; import sys; print(Path(sys.argv[1]).resolve())' "$1")"
PYTHON_VERSION="${PYTHON_VERSION:-3.12}"
WORKDIR="$(mktemp -d)"
trap 'rm -rf "$WORKDIR"' EXIT

cd "$WORKDIR"
UV_CACHE_DIR="${UV_CACHE_DIR:-/tmp/ramp_python_uv_cache}" uv run --no-project \
    --python "$PYTHON_VERSION" \
    --with "$WHEEL_PATH" \
    python - <<'PY'
from ramp import AsyncRamp, Ramp
from ramp._generated.agent_tools import OPERATION_METADATA


assert Ramp.__name__ == "Ramp"
assert AsyncRamp.__name__ == "AsyncRamp"
assert OPERATION_METADATA
assert "agent_tools.bills.list" in OPERATION_METADATA
print("ramp-python wheel smoke test passed")
PY
