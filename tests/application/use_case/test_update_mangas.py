from uuid import UUID

from manga_tracker.application.use_case._update_mangas import UpdateMangasUseCase
from tests.fake.crawler import FakeCrawler
from tests.fake.repository import FakeMangaRepository

DEFAULT_IDS = [
    UUID("83940b5b-79ac-4ac1-8486-41f0b180bd87"),
    UUID("6205bb33-c2a5-486f-bebf-0948096b6303"),
    UUID("7d442d7d-78be-476a-ad93-9efff96bd9b6"),
    UUID("40facf0c-7882-4b63-b490-74e05b2a4b33"),
    UUID("f900baa0-4ccc-4113-8a0e-679fd28b262a"),
]


class TestUpdateMangasUseCase:
    def test_execute_whenCalled_persistAllCrawledMangeToRepository(self) -> None:
        mock_manga_repository = FakeMangaRepository()
        stub_crawler = FakeCrawler(ids=DEFAULT_IDS)
        updater = UpdateMangasUseCase(
            crawlers=[stub_crawler],
            repository=mock_manga_repository,
        )

        updater.execute()

        assert all(id in mock_manga_repository.mangas for id in DEFAULT_IDS)
