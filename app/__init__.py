from flask import Flask
from app.configs import database, migrations
from environs import Env

env = Env()
env.read_env()

def create_app():
    app = Flask(__name__)

    database.init_app(app)
    migrations.init_app(app)


