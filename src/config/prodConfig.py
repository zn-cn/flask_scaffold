from config.baseConfig import BaseConfig


class ProdConfig(BaseConfig):
    def __init__(self):
        super(ProdConfig, self).__init__()

        self.DEBUG = True

        self.SECRET = 'mysecret'

        self.MYSQL_HOST = 'mysql'
        self.REDIS_HOST = 'redis'
        self.DEFAULT_DB_NAME = 'flask_test'
        self.DEFAULT_DB_USER = 'molscar'
        self.DEFAULT_DB_PASSWD = 'molscar_password'

        self.LOG_PATH = "/app/log/"