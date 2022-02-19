from flask import request,current_app,jsonify
from app.models.recipe_model import RecipeModel
from app.utils import check_user


def create_recipe():
    session = current_app.db.session

    data = request.get_json()

    recipe = RecipeModel(**data)

    session.add(recipe)
    session.commit()

    return jsonify(recipe),201


def list_recipes():
    all_recipes = RecipeModel.query.all()

    response = [recipe.serialize() for recipe in all_recipes]

    return jsonify(response),200

def get_recipe(id):
    recipe:RecipeModel = check_user(id,RecipeModel,"recipe")

    return jsonify(recipe.serialize()),200