from typing import Generator
from bs4 import BeautifulSoup
from requests.utils import requote_uri
from .matcher import Matcher
from .. import share


class BingMatcher(Matcher):
    def match(
        self, bs4obj: BeautifulSoup
    ) -> Generator[tuple[str, str, str], None, None]:
        objs = (
            bs4obj.find("div", {"id": "b_content"})
            .find("main")
            .find("ol", {"id": "b_results"})
        )

        for obj in objs.find_all("li", {"class": "b_algo"}):
            href = None
            content = ""
            title = None

            href = (
                obj.find("div", {"class": "b_tpcn"})
                .find("a", {"class": "tilk"})
                .get("href")
            )
            title = obj.find("h2").find("a").text
            try:
                for i in list((obj.find("div", {"class": "b_caption"}).find("p")))[2:]:
                    if isinstance(i, str):
                        content += i
                    else:
                        content += i.text
            except:
                share.TOTAL_ERR += 1
                content = ""
            if not isinstance(content, str):
                content = ""
            if not isinstance(title, str):

                title = None
            if not isinstance(href, str):
                href = None
            yield (title, href, content)

    def get_url(self) -> str:
        return requote_uri(f"https://www.bing.com/search?q={self._question}")
