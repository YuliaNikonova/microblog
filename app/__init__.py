import os
from flask import Flask, redirect, url_for, render_template
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.login import LoginManager, UserMixin, login_user, logout_user, current_user
from flask.ext.openid import OpenID
from oauth import OAuthSignIn
from config import basedir

app = Flask(__name__)
app.config.from_object('config')
app.config['OAUTH_CREDENTIALS'] = {
    'facebook': {
        'id': '999659110055225',
        'secret': '36550d360347e840e6a018739664700d'
    }
}


db = SQLAlchemy(app)
lm = LoginManager()
lm.init_app(app)
lm.login_view = 'login'
oid = OpenID(app, os.path.join(basedir, 'tmp'))

from app import views, models
