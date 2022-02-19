from flask import Flask
from app.routes.recipe_blueprint import bp as bp_recipes
from app.routes.ingredient_blueprint import bp as bp_ingredients
from app.routes.super_market_bp import bp_supermarkets
from app.routes.product_blueprint import bp as bp_products

def init_app(app:Flask):
    app.register_blueprint(bp_recipes)
    app.register_blueprint(bp_ingredients)
    app.register_blueprint(bp_supermarkets)
    app.register_blueprint(bp_products)
    
