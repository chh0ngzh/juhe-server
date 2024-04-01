from urllib.parse import parse_qs
from urllib.parse import urlparse


def get_url_query(url: str) -> str:
    return urlparse(url).query


def get_query_value(qs: str) -> dict:
    return dict([(k, v[0]) for k, v in parse_qs(qs).items()])
