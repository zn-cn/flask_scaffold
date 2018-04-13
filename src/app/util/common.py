# -*- coding: utf-8 -*-
"""
    app.util.common
    定义一般的工具函数
"""
import jwt
from functools import wraps
import json
from flask import request
from app.model.log import Logger
from app.model.ret_code import RetCode
from app.model.ret_msg import RetMessage
from config import CONFIG

common_logger = Logger(dir_name="app/util/common", file_name="app.util.common")


def inject_args(params=None, can_empty=True):
    """
        获取args参数
    """

    def decorator(func):
        @wraps(func)
        def decorated_function(*args, **kwargs):
            data = {}
            raw_args = request.args
            for arg in params:
                data[arg] = raw_args.get(arg, "")
                if not data[arg] and not can_empty:
                    common_logger.error(RetMessage.PARAMS_ERROR)
                    return ret_json(
                        ret_code=RetCode.PARAMS_ERROR,
                        error_msg=RetMessage.PARAMS_ERROR)

            response = func(data, *args, **kwargs)
            return response

        return decorated_function

    return decorator


def inject_json(params=None, can_empty=True):
    """
        获取json参数
    """

    def decorator(func):
        @wraps(func)
        def decorated_function(*args, **kwargs):
            data = {}
            json_data = request.json
            for arg in params:
                data[arg] = json_data.get(arg, "")
                if not data[arg] and not can_empty:
                    common_logger.error(RetMessage.PARAMS_ERROR)
                    return ret_json(
                        ret_code=RetCode.PARAMS_ERROR,
                        error_msg=RetMessage.PARAMS_ERROR)
            response = func(data, *args, **kwargs)
            return response

        return decorated_function

    return decorator


def inject_form(params=None, can_empty=True):
    """
        获取json参数
    """

    def decorator(func):
        @wraps(func)
        def decorated_function(*args, **kwargs):
            data = {}
            form_data = request.form
            for arg in params:
                data[arg] = form_data.get(arg, "")
                if not data[arg] and not can_empty:
                    common_logger.error(RetMessage.PARAMS_ERROR)
                    return ret_json(
                        ret_code=RetCode.PARAMS_ERROR,
                        error_msg=RetMessage.PARAMS_ERROR)
            response = func(data, *args, **kwargs)
            return response

        return decorated_function

    return decorator


def ret_json(ret_code=RetCode.NO_ERROR, error_msg=RetMessage.NO_ERROR,
             data=""):
    ret = {"ret_code": ret_code}
    if ret_code != RetCode.NO_ERROR:
        # 错误信息
        ret["error_msg"] = error_msg
    if data != "":
        ret["data"] = data
    return json.dumps(ret)


def get_token(payload, secret=CONFIG.SECRET, algorithm=CONFIG.JWT_ALGORITHM):
    return jwt.encode(payload=payload, key=secret, algorithm=algorithm)
