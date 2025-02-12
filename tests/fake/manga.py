__all__ = ["create_fake_manga"]

from uuid import UUID

from manga_tracker.domain import Manga


def create_fake_manga(id: UUID) -> Manga:
    return Manga(
        id=id,
        name="SomeManga",
        author="Test",
        source="Site",
        link="https://example.com/SomeManga",
        latest_chapter=27,
        updated=1739353123.66578,
    )
