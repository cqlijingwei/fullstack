from services.user.salary_info import (search_info, user_edit, user_del, user_add)
from units.response import fail_response, success_response
from . import api
from flask import request


@api.route("/user/search", methods=["GET"])
def search():
    kwargs = dict(request.args)
    if not kwargs:
        return fail_response(-2)
    res = search_info(kwargs)
    return success_response(data=res)


@api.route("/user/edit", methods=["POST"])
def edit():
    kwargs = dict(request.json)
    if not kwargs:
        return fail_response(-2)
    res = user_edit(kwargs)
    if not res:
        return fail_response()
    return success_response()


@api.route("/user/del", methods=["POST"])
def del_user():
    kwargs = dict(request.json)
    if not kwargs:
        return fail_response(-2)
    res = user_del(kwargs)
    if not res:
        return fail_response()
    return success_response()


@api.route("/user/add", methods=["POST"])
def add_user():
    kwargs = dict(request.json)
    if not kwargs:
        return fail_response(-2)
    res = user_add(kwargs)
    if not res:
        return fail_response()
    return success_response()
