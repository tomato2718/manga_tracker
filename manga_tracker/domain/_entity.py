__all__ = ["Manga"]

from dataclasses import dataclass


@dataclass(slots=True)
class Manga:
    id: bytes
    name: str
    author: str
    source: str
    link: str
    latest_chapter: int
    updated: float
