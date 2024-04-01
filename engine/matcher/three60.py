from typing import Generator
from bs4 import BeautifulSoup

from ..utils.web import get_element_by_cls, get_element_by_ids
from .matcher import Matcher
from .. import share


class Three60Matcher(Matcher):
    def get_url(self) -> str:
        return "https://so.com/s?q=" + self._question

    def match(
        self, bs4obj: BeautifulSoup
    ) -> Generator[tuple[str, str, str], None, None]:

        main = get_element_by_ids(bs4obj, "div", "warper", "container", "main")

        ul = get_element_by_cls(main, "ul", "result")

        if ul is None:
            yield (None, None, None)
        else:
            for li in ul.find_all("li", {"class": "res-list"}):
                li: BeautifulSoup

                title = None
                content = ""
                url = None

                if li is None:
                    share.TOTAL_ERR += 1
                    continue

                # url
                url = li.find("h3").find("a").get("data-mdurl")
                if url is None:
                    continue

                # title
                title = li.find("h3").find("a").text
                if title is None:
                    continue

                # content
                div = li.find("div", {"class": "res-rich"})
                if div is None:
                    continue

                if len(div) == 2:
                    div = list(div.children)[1]

                div = list(div.children)[3:-2]

                for item in div:
                    content += item.text.strip().replace(" ", "").replace("\n", "")

                yield (title, url, content)
