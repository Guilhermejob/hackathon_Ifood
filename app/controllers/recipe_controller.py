from flask import request,current_app,jsonify
from app.models.recipe_model import RecipeModel
from app.utils import check_user,check_data
from app.exceptions import NotFoundError,InvalidIdValueError,InvalidDataError


def create_recipe():
    session = current_app.db.session

    body = request.get_json()
    try:
        data = check_data(body,RecipeModel.mandatory_data)
        data["name"] = data["name"].title()

    except InvalidDataError as err:
        return jsonify(err.message),400

    recipe = RecipeModel(**data)

    session.add(recipe)
    session.commit()

    return jsonify({"msg":"successfully created", "data":recipe}),201


def list_recipes():
    all_recipes = RecipeModel.query.all()

    response = [recipe.serialize() for recipe in all_recipes]

    return jsonify(response),200

def get_recipe(id):
    try:
        recipe:RecipeModel = check_user(id,RecipeModel,"recipe")

    except NotFoundError as error:
        return jsonify(error.message),404
    except InvalidIdValueError as error:
        return jsonify(error.message),400

    return jsonify(recipe.serialize()),200


def get_recipes_by_name(name):
    recipe_list:list[RecipeModel] = RecipeModel.query.filter(RecipeModel.name.ilike(f"%{name}%")).all()

    response = [recipe.serialize() for recipe in recipe_list]

    return jsonify(response),200