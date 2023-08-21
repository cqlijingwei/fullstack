from flask import jsonify

MSG = {
    0: "request_success",
    1: "request_fail",
    2: "params miss",

}


def response(code, msg, data, headers):
    ret_msg = {
        "code": code,
        "msg": MSG.get(code) or msg,
        "data": data,
    }
    return jsonify(ret_msg), headers


def success_response(code=0, msg="request_success", data=None, headers={}):
    return response(code, msg, data, headers)


def fail_response(code=1, msg="request_fail", data=None, headers={}):
    return response(code, msg, data, headers)
