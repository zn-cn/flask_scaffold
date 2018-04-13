from werkzeug.security import generate_password_hash, check_password_hash

from app.handler.base import conn
from app.model.log import Logger

user_logger = Logger(dir_name="app/handler/user", file_name="app.handler.user")


@conn
def add_user(cur, username, passwd, email):
    pw_hash = generate_password_hash(passwd)
    sql = 'INSERT INTO `user`(username, password, email) VALUES (%s, %s, %s)'
    values = (username, pw_hash, email)
    cur.execute(sql, values)


@conn
def get_passwd(cur, username):
    sql = 'SELECT password from user WHERE username=%s'
    values = (username, )
    cur.execute(sql, values)


@conn
def get_email(cur, username):
    sql = 'SELECT email from user WHERE username=%s'
    values = (username, )
    cur.execute(sql, values)
    return cur.fetchone()


def is_passwd_valid(username, passwd):
    pw_hash = get_passwd(username)
    if pw_hash:
        return check_password_hash(pw_hash[0], passwd)
    return False
