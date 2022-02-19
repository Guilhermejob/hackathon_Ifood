from app.configs.database import db
from dataclasses import dataclass
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship, backref


@dataclass
class SupermarketModel(db.Model):
    id:int
    name:str

    __tablename__ = 'supermarkets'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, unique=True)
    products = relationship(
        "ProductModel", backref=backref("supermarket", uselist=False))

