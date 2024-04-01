from flask import Blueprint

from ..utils.common import build_json, API_OK, API_ARG_FAILED
from ..matcher.google import GoogleMatcher
from ..matcher.bing import BingMatcher
from ..matcher.three60 import Three60Matcher
from ..utils.web import get_web_page, make_document_tree
from .. import share

bp = Blueprint("Matcher", __name__, url_prefix="/matcher")


@bp.route("/all")
def page_matcher():
    obj = {"matchers": ["google", "bing", "360"]}
    return build_json(API_OK, obj)


@bp.route("/<matcher>/query/<keyword>")
def matcher(matcher, keyword):
    matcher_calss = None

    if matcher == "google":
        matcher_calss = GoogleMatcher
    elif matcher == "bing":
        matcher_calss = BingMatcher
    elif matcher == "360":
        matcher_calss = Three60Matcher
    else:
        return build_json(API_ARG_FAILED, {"msg": "不存在的matcher!"})
    # Build Matcher class

    m_matcher = matcher_calss(keyword)

    web_content = make_document_tree(get_web_page(m_matcher.get_url()))

    res = list(m_matcher.match(web_content))

    share.TOTAL_REQ_COUNT += 1

    return build_json(API_OK, {"result": res})
