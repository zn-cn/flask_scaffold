from config.baseConfig import BaseConfig


class ProdConfig(BaseConfig):
    def __init__(self):
        super().__init__()

        self.DEBUG = False

        self.SECRET = 'mysecret'
        self.MYSQL_PORT = 3306
        self.MYSQL_HOST = 'mysql'
        self.REDIS_HOST = 'redis'
        self.REDIS_PORT = 6379
        self.DB_NAME = 'flask_test'
        self.DB_USER = 'molscar'
        self.DB_PASSWD = 'molscar_password'

        self.LOG_PATH = "/app/log/"