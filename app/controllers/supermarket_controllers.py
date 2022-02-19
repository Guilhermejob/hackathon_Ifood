from flask import jsonify, request, current_app
from app.models.supermarket_model import SupermarketModel

def create():
    data = request.get_json()

    supermarket = SupermarketModel(**data)

    current_app.db.session.add(supermarket)
    current_app.db.session.commit()

    return jsonify({"msg":"successfully created", "data":supermarket}), 201

def get_all_supermarkets():
    all_markets = SupermarketModel.query.all()
    return jsonify(all_markets), 200



