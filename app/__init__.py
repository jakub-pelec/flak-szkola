from flask import Flask
from flask_dance.contrib.github import make_github_blueprint
import secrets
import os

app = Flask(__name__)

app.secret_key = secrets.token_hex(16)
os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'

blueprint = make_github_blueprint(
    client_id="011c8dcc882ac8d13827",
    client_secret="4fac0e706ba2430a0ef60e5c59b87c38fb382a3b",
)
app.register_blueprint(blueprint, url_prefix="/login")

from app import views