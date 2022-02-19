from flask import Flask
from flask_migrate import Migrate

def init_app(app:Flask):
    from app.models.supermarket_model import SupermarketModel
    from app.models.product_model import ProductModel


    Migrate(app, app.db)