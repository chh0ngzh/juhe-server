from json import dumps
from .. import share

API_OK = 0
API_ARG_FAILED = 1


def list_visits(obj, *cnt: int) -> object:
    for c in cnt:
        try:
            obj = list(obj)[c]
        except IndexError:
            share.TOTAL_ERR += 1

            break

    return obj


def build_json(code: int, data: dict):
    return dumps({"code": code, "data": data}, ensure_ascii=False)
