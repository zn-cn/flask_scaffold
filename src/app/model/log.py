# -*- coding: utf-8 -*-
"""
    app.model.log
    定义log操作工具
"""

from logging.handlers import RotatingFileHandler

from config import CONFIG

import logging
import os

# 定义log文件的位置
LOG_PATH = CONFIG.LOG_PATH


class Logger(object):
    """
        :param object: 继承的对象
        :return:
    """

    def __init__(self, dir_name, file_name):
        """
            :param dir_name:
            :param file_name:
            :summary 初始化对象
        """
        self.__logger = self._get_logger(dir_name, file_name)

    def debug(self, message):
        """
            :param message:
            :summary: debug record
        """
        self.__logger.debug(message)

    def info(self, message):
        """
            :param message:
            :return:
        """
        self.__logger.info(message)

    def warn(self, message):
        """
            :param message:
            :summary: warning record
        """
        self.__logger.warn(message)

    def error(self, message):
        """
            :param message:
            :summary: error record
        """
        self.__logger.error(message)

    @staticmethod
    def _makedir(dir_name):
        """
            :param dir_name:
            :summary: 创建log文件
        """
        log_dir = "%s%s" % (LOG_PATH, dir_name)
        is_exist = os.path.exists(log_dir)
        if not is_exist:
            os.makedirs(log_dir)
        return log_dir

    @staticmethod
    def _get_logger(dir_name, file_name):
        """
            :param dir_name: 文件夹名
            :param file_name: 文件名
            :summary: 获取logger操作句柄
        """
        dir_name = Logger._makedir(dir_name)
        log_operate = logging.getLogger(file_name)
        log_operate.setLevel(logging.DEBUG)

        # 定义控制台的log形式
        console = logging.StreamHandler()
        console.setLevel(logging.INFO)
        formatter = logging.Formatter(
            "[%(levelname)s: %(asctime)s] %(filename)s %(lineno)d %(message)s")
        console.setFormatter(formatter)
        log_operate.addHandler(console)

        # 定义文件的log形式
        file_handler = RotatingFileHandler(
            "%s/%s.log" % (dir_name, file_name),
            maxBytes=5 * 1024 * 1024,
            backupCount=10)
        file_handler.setLevel(logging.DEBUG)
        formatter = logging.Formatter(
            "[%(levelname)s: %(asctime)s] %(filename)s %(lineno)d %(message)s")
        file_handler.setFormatter(formatter)
        log_operate.addHandler(file_handler)

        return log_operate
