from flask import Blueprint
from app.controllers.ingredient_controller import create_ingredient

bp = Blueprint("bp_ingredient",__name__)

bp.post("/ingredient")(create_ingredient)
