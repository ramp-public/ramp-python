"""Public exceptions raised by the Ramp SDK."""

from __future__ import annotations


class RampError(Exception):
    """Base class for Ramp SDK failures."""


class APIStatusError(RampError):
    """Ramp returned a non-successful HTTP response."""

    def __init__(self, message: str, *, status_code: int) -> None:
        super().__init__(message)
        self.status_code = status_code


class AuthenticationError(APIStatusError):
    """Ramp rejected the supplied authentication credentials."""
