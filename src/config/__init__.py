import os

from config.devConfig import DevConfig
from config.prodConfig import ProdConfig


def load_config(env='debug'):
    configs = {'dev': DevConfig, 'prod': ProdConfig}
    Config = configs[env]
    return Config


Config = load_config(os.environ.get('WEB_ENV', "dev"))
CONFIG = Config()
