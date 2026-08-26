"""Small handwritten runtime boundary used by the generated SDK surface."""

from __future__ import annotations

from dataclasses import dataclass
from os import PathLike
from typing import Any, Protocol, TypeAlias


class NotGiven:
    """Sentinel distinguishing an omitted argument from an explicit null."""

    __slots__ = ()

    def __repr__(self) -> str:
        return "NOT_GIVEN"


NOT_GIVEN = NotGiven()
FileInput: TypeAlias = bytes | PathLike[str]


@dataclass(frozen=True, slots=True)
class OperationMetadata:
    operation_id: str
    scopes: tuple[str, ...]
    platforms: tuple[str, ...]
    stability: str
    pagination: str
    safety: str
    gate: str | None


class SyncTransport(Protocol):
    def request(
        self,
        *,
        method: str,
        path: str,
        path_params: dict[str, Any] | None,
        params: dict[str, Any] | None,
        headers: dict[str, Any] | None,
        json: dict[str, Any] | None,
        data: dict[str, Any] | None,
        files: dict[str, FileInput] | None,
        metadata: OperationMetadata,
    ) -> object: ...


class AsyncTransport(Protocol):
    async def request(
        self,
        *,
        method: str,
        path: str,
        path_params: dict[str, Any] | None,
        params: dict[str, Any] | None,
        headers: dict[str, Any] | None,
        json: dict[str, Any] | None,
        data: dict[str, Any] | None,
        files: dict[str, FileInput] | None,
        metadata: OperationMetadata,
    ) -> object: ...
