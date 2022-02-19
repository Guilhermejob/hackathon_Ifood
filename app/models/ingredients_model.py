from app.configs.database import db
from dataclasses import dataclass
from sqlalchemy import Column, Integer, String
from sqlalchemy.sql.schema import ForeignKey

@dataclass
class IngredientModel(db.Model):
    product:str
    quantity:int

    __tablename__ = 'ingredients'

    id = Column(Integer, primary_key=True)
    product = Column(String, nullable=False)
    quantity = Column(String,default='não especificado')

    recipe_id = Column(Integer,ForeignKey('recipes.id'))

    mandatory_data = {
        "product":str,
        "quantity":str,
        "recipe":str
    }

    def serialize(self):
        return{
            "ingredientId":self.id,
            "product":self.product,
            "quantity":self.quantity,
            "recipe":self.recipe
        }