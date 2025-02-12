__all__ = ["MangaRepository"]

from collections.abc import Iterable
from typing import Generic, Protocol, TypeVar

from ._entity import Manga


class MangaRepository(Protocol):
    def upsert_many(self, mangas: Iterable[Manga]) -> "Result[None, None]": ...

    def search_by_author(self, author: str) -> "Result[list[Manga], None]": ...


DataType = TypeVar("DataType")
FailType = TypeVar("FailType", covariant=True)


class Result(Protocol, Generic[DataType, FailType]):
    def is_ok(self) -> bool: ...

    def unwrap(self) -> DataType: ...

    def unwrap_fail(self) -> FailType: ...

    def unwrap_or(self, default: DataType) -> DataType: ...
