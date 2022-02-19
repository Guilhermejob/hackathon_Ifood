from flask import Blueprint
from app.controllers.supermarket_controllers import create, get_all_supermarkets,get_supermarket_by_id

bp_supermarkets = Blueprint('bp_supermarkets', __name__)

bp_supermarkets.post('/supermarkets')(create)
bp_supermarkets.get('/supermarkets')(get_all_supermarkets)
bp_supermarkets.get('/supermarkets/<int:id>')(get_supermarket_by_id)