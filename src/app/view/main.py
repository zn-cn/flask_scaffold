import datetime
import json
import jwt
import logging
import re

from flask import Blueprint
from flask import request

from config import config
from app.view.base import login_required, cached
from app.handler.user import add_user, get_email, is_passwd_valid

from app.model.log import Logger

main_logger = Logger(dir_name="app/view/main", file_name="app.view.main")

main_view = Blueprint('main', __name__)

email_pat = re.compile(r'^[\d,a-z]([\w\.\-]+)@([a-z0-9\-]+).([a-z\.]+[a-z])$')


@main_view.route('/users', methods=['GET', 'POST'])
def register():
    data = request.json
    username = data.get('username')
    password = data.get('password')
    email = data.get('email')
    if email_pat.match(email) is None:
        return json.dumps({
            'successful': False,
            'error': 'Invalid email address!'
        })
    try:
        add_user(username, password, email)
    except Exception as e:
        logging.warn('register error: ' + e.message)
        return json.dumps({
            'successful': False,
            'error': 'Email already registered!'
        })
    token = jwt.encode(
        {
            'username': username,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(days=7)
        },
        config.SECRET,
        algorithm=config.JWT_ALGORITHM)
    return json.dumps({'successful': True, 'data': {'token': token}})


@main_view.route('/login', methods=['GET', 'POST'])
def login():
    token = request.headers.get('Authorization')
    try:
        payload = jwt.decode(
            token, config.SECRET, algorithms=[config.JWT_ALGORITHM])
    except Exception as e:
        logging.warn('login error: ' + e.message)
        return json.dumps({
            'successful': False,
            'error': 'Invalid username or password'
        })
    if payload:
        username = payload.get('username')
        logging.info(username)
    else:
        data = request.json
        username = data.get('username')
        password = data.get('password')
        if not is_passwd_valid(username, password):
            return json.dumps({
                'successful': False,
                'error': 'Invalid username or password'
            })
    token = jwt.encode(
        {
            'username': username,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(days=7)
        },
        config.SECRET,
        algorithm=config.JWT_ALGORITHM)
    return json.dumps({'successful': True, 'data': {'token': token}})


@main_view.route('/emails/<username>')
@login_required
@cached()
def get_emails(username):
    email = get_email(username)
    return json.dumps({'successful': True, 'data': email})
