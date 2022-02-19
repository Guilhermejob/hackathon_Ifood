from flask import request,current_app,jsonify
from app.models.ingredients_model import IngredientModel
from app.models.recipe_model import RecipeModel
from app.utils import check_user


def create_ingredient():
    session = current_app.db.session

    data = request.get_json()
    recipe_name = data.pop('recipe')

    recipe = RecipeModel.query.filter_by(name=recipe_name).first()

    data['recipe_id'] = recipe.id

    ingredient = IngredientModel(**data)

    session.add(ingredient)
    session.commit()

    return jsonify(ingredient),201


def list_ingredients_by_recipe(id):
    recipe:RecipeModel = check_user(id,RecipeModel,"recipe")

    return jsonify(recipe.ingredients),200