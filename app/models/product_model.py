from app.configs.database import db
from dataclasses import dataclass
from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.sql.schema import ForeignKey


@dataclass
class ProductModel(db.Model):
    id:int
    name:str
    price:str
    super_market_id:int

    __tablename__ = 'products'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, unique=True)
    price = Column(Float, nullable=False)
    super_market_id  = Column(Integer, ForeignKey(
        'supermarkets.id'))

