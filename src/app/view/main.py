from flask import Blueprint
from flask import request

from app.view.base import login_required
from app.handler.user import add_user
from app.handler.user import real_login
from app.handler.user import get_email
from app.model.log import Logger
from app.util.common import inject_json

main_view = Blueprint('main', __name__)


@main_view.route('/register', methods=['POST'])
@inject_json(params=["username", "password", "email"], can_empty=False)
def register(data):
    result = add_user(
        username=data.get('username'),
        passwd=data.get('password'),
        email=data.get('email'))
    return result


@main_view.route('/login', methods=['POST'])
@inject_json(params=["username", "password"], can_empty=False)
def login(data):
    result = real_login(
        username=data.get("username"), password=data.get("password"))
    return result


@main_view.route('/emails')
@login_required
def get_emails(payload):
    username = payload.get("username", "")
    email = get_email(username)
    return email
