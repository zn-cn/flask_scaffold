from functools import wraps
import pymysql

from config import config


def conn(func):
    @wraps(func)
    def wrapper(*args, **kw):
        db = pymysql.connect(config.MYSQL_HOST, config.DEFAULT_DB_USER,
                             config.DEFAULT_DB_PASSWD, config.DEFAULT_DB_NAME)
        cur = db.cursor(pymysql.cursors.DictCursor)
        rv = func(cur, *args, **kw)
        db.commit()
        db.close()
        return rv

    return wrapper
