from flask import Flask
from app.views.MainView import main_view

def configure_blueprints(app):
    app.secret_key = 'test'
    blueprints = {main_view: '/api/v1'}
    for key in blueprints:
        app.register_blueprint(key, url_prefix=blueprints[key])

app = Flask(__name__)
configure_blueprints(app)