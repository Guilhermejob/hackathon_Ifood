from flask import Blueprint
from app.controllers.products_controller import register_product

bp = Blueprint("bp_product",__name__)

bp.post("/products")(register_product)
