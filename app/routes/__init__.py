from flask import Flask
from .recipe_blueprint import bp as bp_recipes
from .ingredient_blueprint import bp as bp_ingredients

def init_app(app:Flask):
    app.register_blueprint(bp_recipes)
    app.register_blueprint(bp_ingredients)