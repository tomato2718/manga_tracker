__all__ = ["JumpplusCrawler"]

from collections.abc import Iterable
from time import time
from typing import cast
from uuid import NAMESPACE_URL, uuid3

from bs4 import BeautifulSoup
from requests import get

from manga_tracker.domain import CrawlerFail, Manga, Result
from manga_tracker.infrastructure.shared.result import Fail, Ok

HEADERS = {
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
}


class JumpplusCrawler:
    __url: str

    def __init__(self, url: str) -> None:
        self.__url = url

    def crawl(self) -> Result[Iterable[Manga], CrawlerFail]:
        response = get(self.__url, headers=HEADERS)
        if response.status_code >= 400:
            return Fail(CrawlerFail.UNACCESSABLE)
        html = response.content.decode()
        return self._parse(html)

    def _parse(self, html: str) -> Result[Iterable[Manga], CrawlerFail]:
        mangas: list[Manga] = []
        soup = BeautifulSoup(html, "html.parser")
        for element in soup.find_all("li", {"class": "series-list-item"}):
            name = cast(
                str, element.find(attrs={"class": "series-list-title"}).get_text()
            )
            author = cast(
                str, element.find(attrs={"class": "series-list-author"}).get_text()
            )
            link = cast(str, element.find("a").get("href"))
            try:
                manga = Manga(
                    id=uuid3(NAMESPACE_URL, link),
                    name=name,
                    author=author,
                    source="Jump+",
                    link=link,
                    latest_chapter=1,
                    updated=time(),
                )
            except Exception:
                return Fail(CrawlerFail.FAIL_TO_PARSE_RESOURCE)
            mangas.append(manga)

        return Ok(mangas)
