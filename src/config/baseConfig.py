# -*- coding : utf-8 -*-


class BaseConfig(object):
    def __init__(self):

        self.DEBUG = False

        self.SECRET = 'hhhhhhhhh'
        self.JWT_ALGORITHM = 'HS256'

        self.REDIS_PORT = 6379
        self.DEFAULT_HOST = 'localhost'

        self.LOG_PATH = "/app/log/"