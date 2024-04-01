from requests import get
from bs4 import BeautifulSoup


def get_web_page(url: str, user_agent: str = "", time_out: float = 1) -> str:
    "Request the page by the url and return the content of string in unicode."

    resp = get(url, timeout=time_out, params={"User-Agent": user_agent})

    return resp.text


def make_document_tree(content: str) -> BeautifulSoup:
    "Build a BeautifulSoup object and return."

    bs4obj = BeautifulSoup(content, features="lxml")

    return bs4obj


def get_element_by_ids(root: BeautifulSoup, type: str, *ids: tuple[str]):
    for name in ids:
        try:
            root = root.find(type, {"id": name})
        except AttributeError:
            return None

    return root


def get_element_by_cls(root: BeautifulSoup, type: str, *ids: tuple[str]):
    for name in ids:
        try:
            root = root.find(type, {"class": name})
        except AttributeError:
            return None

    return root
