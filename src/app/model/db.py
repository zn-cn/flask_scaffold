# -*- coding: utf-8 -*-
"""

    app.model.db
    定义Mongo操作

"""

import traceback

import pymysql.cursors
from config import CONFIG


class DBModel(object):
    """
        数据库操作
    """

    def __init__(self,
                 db_name=CONFIG.DB_NAME,
                 host=CONFIG.MYSQL_HOST,
                 port=CONFIG.MONGO_PORT,
                 user=CONFIG.DB_USER):

        self.conn = pymysql.connect(
            host=host,
            user=user,
            db=db_name,
            charset="utf8mb4",
            cursorclass=pymysql.cursors.DictCursor)
        self.conn_cursor = self.conn.cursor()
