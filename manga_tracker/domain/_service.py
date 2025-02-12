__all__ = ["Crawler"]

from collections.abc import Iterable
from typing import Protocol

from ._entity import Manga


class Crawler(Protocol):
    def crawl(self) -> Iterable[Manga]: ...
