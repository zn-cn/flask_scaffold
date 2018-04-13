import jwt

from functools import wraps
from flask import jsonify, request
from redis import Redis
from config import CONFIG
from app.model.log import Logger
from app.model.ret_code import RetCode
from app.model.ret_msg import RetMessage
from app.util.common import ret_json

base_logger = Logger(dir_name="app/view/base", file_name="app.view.base")

redis = Redis(host=CONFIG.REDIS_HOST, port=CONFIG.REDIS_PORT)


def login_required(func):
    @wraps(func)
    def wrapper(*args, **kw):
        token = request.headers.get('Authorization')
        try:
            payload = jwt.decode(
                token, CONFIG.SECRET, algorithms=[CONFIG.JWT_ALGORITHM])
        except Exception:
            base_logger.error(RetMessage.NOT_AUTH)
            return ret_json(
                ret_code=RetCode.NOT_AUTH, error_msg=RetMessage.NOT_AUTH)
        return func(payload, *args, **kw)

    return wrapper
