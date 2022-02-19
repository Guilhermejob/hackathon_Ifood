from app.configs.database import db
from dataclasses import dataclass
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship


@dataclass
class SupermarketModel(db.Model):
    id:int
    name:str

    __tablename__ = 'supermarkets'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, unique=True)
    products = relationship(
        "ProductModel", backref="supermarket", uselist=True)

    mandatory_data = {
        "name":str,
    }


    def serialize(self):
        return {
            "id":self.id,
            "name":self.name,
            "products_list":[{"id":product.id,"name": product.name} for product in self.products]
        }

