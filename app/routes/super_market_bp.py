from flask import Blueprint
from app.controllers.supermarket_controllers import create, get_all_supermarkets

bp_supermarkets = Blueprint('bp_supermarkets', __name__, url_prefix='/supermarkets')

bp_supermarkets.get('')(get_all_supermarkets)
bp_supermarkets.post('')(create)
