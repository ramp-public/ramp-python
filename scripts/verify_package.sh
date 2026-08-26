#!/bin/bash

set -euo pipefail

PROJECT_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
DIST_DIR="${1:-$PROJECT_ROOT/dist}"
BUILD_DIST="$(mktemp -d)"

cleanup() {
    rm -rf "$BUILD_DIST"
}
trap cleanup EXIT

UV_CACHE_DIR="${UV_CACHE_DIR:-$PROJECT_ROOT/.uv-cache}" uv build --no-config \
    "$PROJECT_ROOT" --out-dir "$BUILD_DIST"

WHEEL_PATH="$(find "$BUILD_DIST" -name 'ramp_python-*.whl' | head -n 1)"
SDIST_PATH="$(find "$BUILD_DIST" -name 'ramp_python-*.tar.gz' | head -n 1)"
test -n "$WHEEL_PATH"
test -n "$SDIST_PATH"

WHEEL_FILES="$(unzip -Z1 "$WHEEL_PATH")"
echo "$WHEEL_FILES" | grep -q '^ramp/__init__.py$'
echo "$WHEEL_FILES" | grep -q '^ramp/py.typed$'
echo "$WHEEL_FILES" | grep -q '/licenses/LICENSE$'

if echo "$WHEEL_FILES" | grep -E '(^|/)(generator|overlay|package\.toml|uv\.lock)($|/)'; then
    echo "Error: wheel contains an internal-only path"
    exit 1
fi

if tar -tzf "$SDIST_PATH" | grep -E '(^|/)(generator|overlay|package\.toml)($|/)'; then
    echo "Error: source distribution contains an internal-only path"
    exit 1
fi

"$PROJECT_ROOT/scripts/library_smoke_tests.sh" "$WHEEL_PATH"

mkdir -p "$DIST_DIR"
cp "$BUILD_DIST"/ramp_python-* "$DIST_DIR"/
