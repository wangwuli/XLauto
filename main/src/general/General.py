import datetime
import json

from flask import jsonify, make_response, Response


class ReturnG:
    def return_false(str):
        return (False, str)

    def return_true(str):
        return (True, str)

    def if_ft(tuple_):
        return tuple_[0]

    def get_value(tuple_):
        return tuple_[1]


class DateEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime.datetime):
            return obj.strftime('%Y-%m-%d %H:%M:%S')
        elif isinstance(obj, datetime.date):
            return obj.strftime("%Y-%m-%d")
        elif isinstance(obj, bytes):
            return str(obj)
        else:
            return json.JSONEncoder.default(self, obj)


class Result():
    success_code = "0"
    fail_code = "1"
    warning_code = "2"

    @staticmethod
    def success(data=[], msg="查询成功", count=-1):
        result = {"code": Result.success_code, "success": True, "data": data, "msg": msg}
        if count != -1:
            result["count"] = count
        return json.dumps(result, cls=DateEncoder)

    @staticmethod
    def success_response(data=[], msg="查询成功", count=-1, cookies={}):
        result = Result.success(data, msg, count)
        response = Response(result, content_type="application/json;charset=utf-8")
        for item in cookies.keys():
            response.set_cookie(item, cookies[item])
        return response

    @staticmethod
    def fail(data, status, msg):
        result = {"code": Result.fail_code, "msg": msg, "success": False, 'data': data}
        return json.dumps(result, cls=DateEncoder)

    @staticmethod
    def fail_response(data="", msg="", status=200):
        result = Result.fail(data, Result.fail_code, msg)
        # return make_response(jsonify(result, status))
        return make_response(result, status)

    @staticmethod
    def warning(data=[], msg=""):
        result = {"code": Result.warning_code, "msg": msg, "success": False, 'data': data}
        return json.dumps(result, cls=DateEncoder)

    @staticmethod
    def warning_response(data=[], msg="", status=200):
        result = Result.fail(data, Result.warning_code, msg)
        # return make_response(jsonify(result, status))
        return make_response(result, status)
