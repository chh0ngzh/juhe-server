from typing import Generator
from bs4 import BeautifulSoup


class Matcher:
    def __init__(self, question: str) -> None:
        self._question = question

    def match(
        self, bs4obj: BeautifulSoup
    ) -> Generator[tuple[str, str, str], None, None]:  # 0: title  1: url 2: content
        ...

    def get_url(self) -> str: ...
