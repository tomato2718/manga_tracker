__all__ = ["run"]

from manga_tracker.application.use_case import UpdateMangasUseCase
from manga_tracker.infrastructure.external.jumpplus_crawler import JumpplusCrawler
from manga_tracker.infrastructure.repository import SQLiteMangaRepository
from manga_tracker.infrastructure.setup import env


def run() -> None:
    with SQLiteMangaRepository(env.SQLITE_PATH) as repo:
        repo.setup()
        update_manga = UpdateMangasUseCase(
            repository=repo,
            crawlers=[JumpplusCrawler(env.JUMPPLUS_URL)],
        )
        update_manga.execute()
