from typing import Generator
from bs4 import BeautifulSoup
from .matcher import Matcher
from ..utils.url import get_url_query, get_query_value
from ..utils.common import list_visits
from requests.utils import requote_uri
from .. import share


class GoogleMatcher(Matcher):
    def match(
        self, bs4obj: BeautifulSoup
    ) -> Generator[tuple[str, str, str], None, None]:
        b = bs4obj.find("div", {"id": "main"})

        content = None
        title = None
        href = None

        for child in list(b)[3:-3]:
            try:
                child = list(list_visits(child, 0))

                header_block = child[0]
                content_block = child[1]

                a_element = list(header_block)[0]

                title_element = list_visits(a_element, 0, 0, 0, 0)

                # content_element = list_visits(content_block, 0, 0, 0, 0, 0)
                content_element = list_visits(content_block, 0, 0, 0)

                if len(content_element) == 2:
                    content_element = list_visits(content_element, 0, 0)
                else:
                    content_element = list_visits(content_element, 0, 0)

                title = (
                    title_element
                    if isinstance(title_element, str)
                    else title_element.text
                )

                # Check the content because there will maybe have time element.
                if len(content_element) == 3:
                    content = list_visits(content_element, 2)
                else:
                    content = content_element.text

                href = a_element.get("href")

                if href:
                    href = get_query_value(get_url_query(href))["q"]

                yield (title, href, content)
            except Exception:
                share.TOTAL_ERR += 1
                yield (None, None, None)

    def get_url(self) -> str:
        return requote_uri(f"https://www.google.com/search?q={self._question}&ie=UTF-8")
