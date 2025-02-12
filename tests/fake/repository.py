__all__ = ["FakeMangaRepository"]

from collections.abc import Iterable
from typing import Any, Generic, TypeVar
from uuid import UUID

from manga_tracker.domain import Manga, Result


class FakeMangaRepository:
    mangas: dict[UUID, Manga]

    def upsert_many(self, mangas: Iterable[Manga]) -> "Result[None, None]":
        for manga in mangas:
            self.mangas[manga.id] = manga
        return Ok(None)

    def search_by_author(self, author: str) -> "Result[list[Manga], None]":
        raise NotImplementedError()


T = TypeVar("T")


class Ok(Generic[T]):
    __data: T

    def __init__(self, data: T, /) -> None:
        self.__data = data

    def is_ok(self) -> bool:
        return True

    def unwrap(self) -> T:
        return self.__data

    def unwrap_fail(self) -> Any:
        raise Exception("Unwrapping Ok Result")

    def unwrap_or(self, default: T) -> T:
        return self.__data
