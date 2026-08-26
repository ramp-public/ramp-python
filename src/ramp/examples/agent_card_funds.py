"""Authenticate a standalone agent and list its eligible Agent Card funds."""

from __future__ import annotations

import argparse
from typing import Literal, cast

from ..client import Ramp

Environment = Literal["sandbox", "production"]


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--environment",
        choices=("sandbox", "production"),
        default="sandbox",
        help="Ramp API environment (default: sandbox)",
    )
    args = parser.parse_args()

    environment = cast(Environment, args.environment)

    with Ramp.from_env(environment=environment) as client:
        result = client.agent_tools.agent_cards.list_funds(
            rationale=(
                "Verify the Python SDK can authenticate and list eligible "
                "Agent Card funds"
            ),
        )

    print("SDK live request succeeded")
    print(f"Response type: {type(result).__name__}")
    print(f"Top-level keys: {sorted(result)}")
    print(f"Eligible fund count: {len(result.get('funds', []))}")


if __name__ == "__main__":
    main()
