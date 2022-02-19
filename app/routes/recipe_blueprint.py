from flask import Blueprint
from app.controllers.recipe_controller import create_recipe,get_recipe,list_recipes

bp = Blueprint("bp_recipe",__name__)

bp.post("/recipe")(create_recipe)
bp.get("/recipe")(list_recipes)
bp.get("/recipe/<int:id>")(get_recipe)