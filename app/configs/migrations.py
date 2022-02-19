from flask import Flask
from flask_migrate import Migrate

def init_app(app:Flask):
    from app.models.supermarket_model import SupermarketModel
    from app.models.product_model import ProductModel
    from app.models.recipe_model import RecipeModel
    from app.models.ingredients_model import IngredientModel


    Migrate(app, app.db)