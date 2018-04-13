import jwt
import logging

from functools import wraps
from flask import jsonify, request
from redis import Redis
from config import config

redis = Redis(host=config.REDIS_HOST, port=config.REDIS_PORT)


def login_required(func):
    @wraps(func)
    def wrapper(*args, **kw):
        token = request.headers.get('Authorization')
        try:
            payload = jwt.decode(
                token, config.SECRET, algorithms=[config.JWT_ALGORITHM])
        except Exception as e:
            logging.warn('login error: ' + e.message)
            return jsonify({'successful': False, 'error': 'Unauthorized!'})
        return func(*args, **kw)

    return wrapper


def cached(timeout=5 * 60, key='view/%s'):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kw):
            cache_key = key % request.url
            logging.info('cache_key: ' + cache_key)
            rv = redis.get(cache_key)
            if rv is not None:
                return rv
            rv = func(*args, **kw)
            redis.set(cache_key, rv)
            return rv

        return wrapper

    return decorator
