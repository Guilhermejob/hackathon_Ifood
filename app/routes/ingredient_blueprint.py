from flask import Blueprint
from app.controllers.ingredient_controller import create_ingredient,create_ingredients_list

bp = Blueprint("bp_ingredient",__name__)

bp.post("/ingredient")(create_ingredient)
bp.post("/ingredient/list")(create_ingredients_list)
