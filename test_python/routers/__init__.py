__all__ = [
    "index"
]

from flask import Blueprint

from routers.api import api

index = Blueprint("/", __name__, url_prefix="/")

index.register_blueprint(api)
# from . import *

