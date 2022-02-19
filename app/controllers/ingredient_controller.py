from itertools import product
from flask import request,current_app,jsonify
from app.models.ingredients_model import IngredientModel
from app.models.recipe_model import RecipeModel
from app.utils import check_data
from app.exceptions import InvalidDataError,InvalidTypeError



def create_ingredient(body):
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

    return jsonify({"msg":"successfully created", "data":ingredient}),201


def validate_list(body):
    ingredients_format = {**IngredientModel.mandatory_data}
    ingredients_format.pop('recipe')

    data_expected = {
        "recipe":"string",
        "ingredients":[ingredients_format]
    }

    if(
        type(body)!=dict or
        not body.get("recipe") or
        type(body["recipe"]) != str or
        not body.get("ingredients") or 
        type(body["ingredients"]) != list
    ):
            raise InvalidTypeError(data_expected)

    ingredients_list = []
    
    for ingredient in body["ingredients"]:
        data = check_data(ingredient,ingredients_format)
        data['product'] = data['product'].capitalize()
        ingredients_list.append(data)
    
    valid_data = {
        "recipe": body["recipe"].title(),
        "ingredients": ingredients_list
    }


    return valid_data


def create_ingredients_list():
    body = request.get_json()

    try:
        recipe_name = body.get("recipe")
        data = validate_list(body)

      
        recipe:RecipeModel = RecipeModel.query.filter(RecipeModel.name.ilike(f"{recipe_name}%")).first()

        session = current_app.db.session
        
        response = []
      

        for ingredient_data in data["ingredients"]:
            ingredient_data['recipe_id'] = recipe.id

            ingredient = IngredientModel(**ingredient_data)

            session.add(ingredient)
            session.commit()

            response.append(ingredient)
        
        return jsonify({"msg":"successfully created", "data":response})
    
    except InvalidDataError as err:
        return jsonify({
            "msg":"one of the fields of an ingredient is wrong",
            "detail": err.message
        }),400

    except InvalidTypeError as err:
        return jsonify(err.message),400




