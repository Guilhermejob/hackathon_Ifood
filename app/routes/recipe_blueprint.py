from flask import Blueprint
from app.controllers.recipe_controller import create_recipe,get_recipe,list_recipes,get_recipes_by_name,get_products_from_recipe

bp = Blueprint("bp_recipe",__name__)

bp.post("/recipe")(create_recipe)
bp.get("/recipe")(list_recipes)
bp.get("/recipe/<int:id>")(get_recipe)
bp.get("/recipe/<string:name>")(get_recipes_by_name)
bp.get("/recipe/<int:id>/products")(get_products_from_recipe)
