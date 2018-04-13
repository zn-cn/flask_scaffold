# -*- coding:utf-8 -*-
"""

    app.model.res_code
    返回状态码

"""


class RetCode(object):
    """
        返回状态码
    """
    NO_ERROR = 2200
    NOT_AUTH = 3000
    ACCESS_TOKEN_ERROR = 3300
    PARAMS_ERROR = 4400
    SERVER_ERROR = 5500
