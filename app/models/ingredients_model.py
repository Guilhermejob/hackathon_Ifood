from app.configs.database import db
from dataclasses import dataclass
from sqlalchemy import Column, Integer, String

@dataclass
class IngredientModel(db.Model):
    id:int
    product:str
    quantity:int

    __tablename__ = 'ingredients'

    id = Column(Integer, primary_key=True)
    product = Column(String, nullable=False)
    quantity = Column(Integer,default=1)

    recipe_id = Column(Integer,db.Foreignkey('recipes.id'))