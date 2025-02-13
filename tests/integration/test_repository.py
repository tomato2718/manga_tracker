from sqlite3 import connect
from uuid import UUID

from manga_tracker.infrastructure.repository._sqlite import SQLiteMangaRepository
from manga_tracker.infrastructure.setup import env
from tests.fake.manga import create_fake_manga

DEFAULT = [
    create_fake_manga(UUID("f900baa0-4ccc-4113-8a0e-679fd28b262a")),
    create_fake_manga(UUID("83940b5b-79ac-4ac1-8486-41f0b180bd87")),
    create_fake_manga(UUID("7d442d7d-78be-476a-ad93-9efff96bd9b6")),
]

UPSERT = [
    create_fake_manga(UUID("f900baa0-4ccc-4113-8a0e-679fd28b262a")),
    create_fake_manga(UUID("83940b5b-79ac-4ac1-8486-41f0b180bd87")),
    create_fake_manga(UUID("7d442d7d-78be-476a-ad93-9efff96bd9b6")),
    create_fake_manga(UUID("6205bb33-c2a5-486f-bebf-0948096b6303")),
    create_fake_manga(UUID("40facf0c-7882-4b63-b490-74e05b2a4b33")),
]


class TestSQLiteMangaRepository:
    @staticmethod
    def setup_repository() -> None:
        connection = connect(env.SQLITE_PATH)
        connection.executemany(
            "INSERT INTO manga VALUES (?, ?, ?, ?, ?, ?, ?)",
            [
                (
                    default.id.bytes,
                    default.name,
                    default.author,
                    default.source,
                    default.link,
                    default.latest_chapter,
                    default.updated,
                )
                for default in DEFAULT
            ],
        )
        connection.commit()
        connection.close()

    def test_upsert_many_givenMangas_persistToDatabase(self) -> None:
        self.setup_repository()

        with SQLiteMangaRepository(env.SQLITE_PATH) as repo:
            result = repo.upsert_many(UPSERT)

        assert result.is_ok()
        connection = connect(env.SQLITE_PATH)
        rows = connection.execute("SELECT id FROM manga").fetchall()
        assert {row[0] for row in rows} == {manga.id.bytes for manga in UPSERT}
        connection.close()
