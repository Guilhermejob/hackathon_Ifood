from flask import jsonify, request, current_app
from app.models.supermarket_model import SupermarketModel
from app.utils import check_data,check_user
from app.exceptions import InvalidDataError,InvalidIdValueError,NotFoundError

def create():
    body = request.get_json()
    try:
        data = check_data(body,SupermarketModel.mandatory_data)
        data["name"] = data["name"].capitalize()
    except InvalidDataError as err:
        return jsonify(err.message),400

    supermarket = SupermarketModel(**data)

    current_app.db.session.add(supermarket)
    current_app.db.session.commit()

    return jsonify({"msg":"successfully created", "data":supermarket}), 201


def get_all_supermarkets():
    all_markets = SupermarketModel.query.all()
    return jsonify(all_markets), 200
    

def get_supermarket_by_id(id):
    try:
        supermarket:SupermarketModel = check_user(id,SupermarketModel,"supermaket")
    except NotFoundError as err:
        return jsonify(err.message),404
    except InvalidIdValueError as err:
        return jsonify(err.message),400

    return jsonify(supermarket.serialize())
