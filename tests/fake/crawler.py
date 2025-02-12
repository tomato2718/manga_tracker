__all__ = ["FakeCrawler"]

from collections.abc import Iterable
from typing import Any
from uuid import UUID

from manga_tracker.domain import CrawlerFail, Manga, Result

from .manga import create_fake_manga

FAKE_DEFAULT_IDS = [
    UUID("83940b5b-79ac-4ac1-8486-41f0b180bd87"),
    UUID("6205bb33-c2a5-486f-bebf-0948096b6303"),
    UUID("7d442d7d-78be-476a-ad93-9efff96bd9b6"),
    UUID("40facf0c-7882-4b63-b490-74e05b2a4b33"),
    UUID("f900baa0-4ccc-4113-8a0e-679fd28b262a"),
]


class FakeCrawler:
    __ids: Iterable[UUID]
    __fail: CrawlerFail | None = None

    def __init__(
        self, ids: Iterable[UUID] = FAKE_DEFAULT_IDS, fail: CrawlerFail | None = None
    ) -> None:
        self.__ids = ids

    def crawl(self) -> Result[Iterable[Manga], "CrawlerFail"]:
        if self.__fail:
            return Fail(self.__fail)
        else:
            return Ok([create_fake_manga(id) for id in self.__ids])


class Ok:
    __data: Iterable[Manga]

    def __init__(self, data: Iterable[Manga], /) -> None:
        self.__data = data

    def is_ok(self) -> bool:
        return True

    def unwrap(self) -> Iterable[Manga]:
        return self.__data

    def unwrap_fail(self) -> Any:
        raise Exception("Unwrapping Ok Result")

    def unwrap_or(self, default: Iterable[Manga]) -> Iterable[Manga]:
        return self.__data


class Fail:
    __fail: CrawlerFail

    def __init__(self, fail: CrawlerFail, /) -> None:
        self.__fail = fail

    def is_ok(self) -> bool:
        return False

    def unwrap(self) -> Any:
        raise Exception("Unwrapping Fail result")

    def unwrap_fail(self) -> CrawlerFail:
        return self.__fail

    def unwrap_or(self, default: Iterable[Manga]) -> Iterable[Manga]:
        return default
