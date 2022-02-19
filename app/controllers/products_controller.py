from flask import jsonify, request, current_app
from app.models.product_model import ProductModel
from app.models.supermarket_model import SupermarketModel


def register_product():
    session = current_app.db.session

    data = request.get_json()

    supermarket_id = data['super_market_id']

    supermarket = SupermarketModel.query.filter_by(id = supermarket_id).first()

    data['super_market_id'] = supermarket.id

    product = ProductModel(**data)

    session.add(product)
    session.commit()

    return jsonify({"msg":"successfully created", "data":product}),201











