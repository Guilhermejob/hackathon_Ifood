from flask import Flask
from app.routes.super_market_bp import bp_supermarkets

def init_app(app:Flask):
    app.register_blueprint(bp_supermarkets)
    return app