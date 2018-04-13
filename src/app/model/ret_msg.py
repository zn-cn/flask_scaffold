# -*- coding:utf-8 -*-
"""

    app.model.res_msg
    返回消息

"""


class RetMessage(object):
    """
        返回消息
    """
    NO_ERROR = "成功"
    NOT_AUTH = "没有认证成功"
    ACCESS_TOKEN_ERROR = "access token 失效"
    PARAMS_ERROR = "参数缺失或者错误"
    SERVER_ERROR = "服务出错"
