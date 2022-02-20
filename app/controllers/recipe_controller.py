from tkinter import S
from flask import request,current_app,jsonify
from app.models.recipe_model import RecipeModel
from app.models.product_model import ProductModel
from app.models.supermarket_model import SupermarketModel
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


def get_products_from_recipe(id):

    
    products = []
    supermarkets_list = []

    response = []
    
    try:
        recipe:RecipeModel = check_user(id,RecipeModel,"recipe")

        for item in recipe.ingredients:

            if item.product[-1] == "s":
                item.product = item.product[0:-1]
            
            product_list =ProductModel.query.filter(ProductModel.name.ilike(f"%{item.product}%")).all()
            products.extend(product_list)

        print(product_list[0].supermarket)

        supermarkets = [item.super_market_id for item in products ]

        supermarkets = set(supermarkets)

        supermarkets = list(supermarkets)

        for id in supermarkets:
            supermarkets_list.append(SupermarketModel.query.get(id))


        for supermarket in supermarkets_list:
            response.append(
                {
                    "supermarket": supermarket,
                    "products":[]
                }           
            )
              

        for item in products:
            for supermarket in response:
                if item.super_market_id == supermarket['supermarket'].id:
                    print(supermarket['products'])
                    supermarket['products'].append(item)
                    

    except NotFoundError as error:
        return jsonify(error.message),404
    except InvalidIdValueError as error:
        return jsonify(error.message),400

    return jsonify (response),200