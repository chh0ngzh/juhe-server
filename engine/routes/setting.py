from time import time
from flask import Blueprint

from sys import version
from os import name
from ..utils.common import build_json, API_OK
from ..__version__ import __version__
from .. import share

bp = Blueprint("System", __name__, url_prefix="/setting")


@bp.route("/")
def setting_p():
    return build_json(
        API_OK,
        {
            "version": f"""Python Version: {version}\nServer Version: {__version__}\nStatus: Running on.\nOperating System:{name}""",
            "status": {
                "uptime": time() - share.START_TIME,
                "total_req": share.TOTAL_REQ_COUNT,
                "total_err": share.TOTAL_ERR,
            },
        },
    )
