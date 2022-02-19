from flask import Flask
from flask_migrate import Migrate

def init_app(app:Flask):
    #aqui vem as models

    Migrate(app, app.db)