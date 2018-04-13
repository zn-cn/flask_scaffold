from werkzeug.security import generate_password_hash, check_password_hash

from app.model.log import Logger
from app.model.db import DBModel
from app.model.ret_code import RetCode
from app.model.ret_msg import RetMessage
from app.util.common import ret_json
from app.util.regex import check_email
from app.util.common import get_token
import datetime
user_logger = Logger(dir_name="app/handler/user", file_name="app.handler.user")
db_cur = DBModel().conn_cursor


def add_user(username, passwd, email):
    if check_email(email) is None:
        return ret_json(
            ret_code=RetCode.PARAMS_ERROR, error_msg=RetMessage.PARAMS_ERROR)
    pw_hash = generate_password_hash(passwd)
    sql = 'INSERT INTO `user`(username, password, email) VALUES (%s, %s, %s)'
    values = (username, pw_hash, email)
    db_cur.execute(sql, values)

    return ret_json(ret_code=RetCode.NO_ERROR)


def get_passwd(username):
    sql = 'SELECT password from user WHERE username=%s'
    values = (username, )
    db_cur.execute(sql, values)
    return db_cur.fetchone().get("password")


def get_email(username):
    sql = 'SELECT email from user WHERE username=%s'
    values = (username, )
    db_cur.execute(sql, values)
    return db_cur.fetchone().get("email")


def is_passwd_valid(username, passwd):
    pw_hash = get_passwd(username)
    if not pw_hash:
        user_logger.error(RetMessage.PARAMS_ERROR)
        return False
    return check_password_hash(pw_hash[0], passwd)


def real_login(username, password):
    if not is_passwd_valid(username, password):
        return ret_json(
            ret_code=RetCode.NOT_AUTH, error_msg=RetMessage.NOT_AUTH)
    token = get_token(
        payload={
            'username': username,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(days=7)
        })
    return ret_json(ret_code=RetCode.NO_ERROR, data={'token': token})