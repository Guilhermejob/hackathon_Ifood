from flask import Blueprint
from app.controllers.ingredient_controller import create_ingredient,list_ingredients_by_recipe

bp = Blueprint("bp_ingredient",__name__)

bp.post("/ingredient")(create_ingredient)
bp.get("/ingredients/recipe/<int:id>")(list_ingredients_by_recipe)