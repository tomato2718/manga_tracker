__all__ = ["MangaRepository"]

from collections.abc import Iterable
from typing import Protocol

from ._common import Result
from ._entity import Manga


class MangaRepository(Protocol):
    def upsert_many(self, mangas: Iterable[Manga]) -> Result[None, None]: ...

    def search_by_author(self, author: str) -> Result[list[Manga], None]: ...
