from flask import Blueprint
from app.controllers.products_controller import register_product,get_product_by_name

bp = Blueprint("bp_product",__name__)

bp.post("/products")(register_product)
bp.get("/products/<string:name>")(get_product_by_name)
