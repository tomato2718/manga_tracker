from collections.abc import Iterable

from manga_tracker.domain import Crawler, Manga, MangaRepository


class UpdateMangasUseCase:
    __crawlers: Iterable[Crawler]
    __repository: MangaRepository

    def __init__(
        self,
        *,
        crawlers: Iterable[Crawler],
        repository: MangaRepository,
    ) -> None:
        self.__crawlers = crawlers
        self.__repository = repository

    def execute(self) -> None:
        mangas: list[Manga] = []

        for crawler in self.__crawlers:
            result = crawler.crawl()
            if result.is_ok():
                mangas.extend(result.unwrap())

        self.__repository.upsert_many(mangas)
