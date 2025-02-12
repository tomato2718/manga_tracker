__all__ = ["Crawler", "CrawlerFail"]

from collections.abc import Iterable
from enum import Enum
from typing import Protocol

from ._common import Result
from ._entity import Manga


class Crawler(Protocol):
    def crawl(self) -> Result[Iterable[Manga], "CrawlerFail"]: ...


class CrawlerFail(Enum):
    UNACCESSABLE = 0
    FAIL_TO_PARSE_RESOURCE = 1
