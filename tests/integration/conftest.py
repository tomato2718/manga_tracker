from typing import Generator

from pytest import fixture

from manga_tracker.infrastructure.repository import (
    SQLiteMangaRepository,
)
from manga_tracker.infrastructure.setup import env


@fixture(scope="function", autouse=True)
def context() -> Generator[None, None, None]:
    with SQLiteMangaRepository(env.SQLITE_PATH) as repo:
        repo.setup()
        yield
        repo.cleanup()
