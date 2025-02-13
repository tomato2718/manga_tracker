__all__ = ["SQLiteMangaRepository"]

from collections.abc import Iterable
from sqlite3 import Connection, connect
from typing import Self

from manga_tracker.domain import Manga, Result

from ._result import Ok
from ._sql import DROP_TABLE, INIT_TABLE, INSERT


class SQLiteMangaRepository:
    __sqlite_path: str
    __sqlite: Connection

    def __init__(self, sqlite_path: str) -> None:
        self.__sqlite_path = sqlite_path

    def __enter__(self) -> Self:
        self.__sqlite = connect(self.__sqlite_path)
        return self

    def __exit__(self, *_) -> None:
        self.__sqlite.close()

    def setup(self) -> None:
        self.__sqlite.execute(INIT_TABLE)

    def cleanup(self) -> None:
        self.__sqlite.execute(DROP_TABLE)

    def upsert_many(self, mangas: Iterable[Manga]) -> "Result[None, None]":
        cursor = self.__sqlite.cursor()
        for manga in mangas:
            cursor.execute(
                INSERT,
                (
                    manga.id.bytes,
                    manga.name,
                    manga.author,
                    manga.source,
                    manga.link,
                    manga.latest_chapter,
                    manga.updated,
                ),
            )
        self.__sqlite.commit()
        return Ok(None)

    def search_by_author(self, author: str) -> "Result[list[Manga], None]":
        raise NotImplementedError()
