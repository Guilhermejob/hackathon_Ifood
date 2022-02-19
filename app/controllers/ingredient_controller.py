from flask import request,current_app,jsonify
from app.models.ingredients_model import IngredientModel
from app.models.recipe_model import RecipeModel
from app.utils import check_user,check_data
from app.exceptions import InvalidDataError



def create_ingredient():
    session = current_app.db.session

    body = request.get_json()
    try:
        data = check_data(body,IngredientModel.mandatory_data)
        data['product'] = data['product'].capitalize()

    except InvalidDataError as err:
        return jsonify(err.message),400

    recipe_name = data.pop('recipe').title()

    recipe = RecipeModel.query.filter_by(name=recipe_name).first()

    data['recipe_id'] = recipe.id

    ingredient = IngredientModel(**data)

    session.add(ingredient)
    session.commit()

    return jsonify(ingredient),201

