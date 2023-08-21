__all__ = [
    "api"
]

from flask import Blueprint

api = Blueprint("/api", __name__, url_prefix="/api")
from .user import *
