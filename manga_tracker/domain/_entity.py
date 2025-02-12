__all__ = ["Manga"]

from dataclasses import dataclass
from uuid import UUID


@dataclass(slots=True)
class Manga:
    id: UUID
    name: str
    author: str
    source: str
    link: str
    latest_chapter: int
    updated: float
