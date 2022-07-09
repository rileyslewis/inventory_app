from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, null
#from sqlalchemy.orm import relationship
from .database import Base



"""
class Inventory(Base):
    __tablename__ = "inventory"

    id = Column(Integer, primary_key=True, index=True)
    category = Column(String, unique=True, index=True)

    items = relationship("Item", back_populates="owner")
"""

class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True, nullable=False)
    quantity = Column(Integer, index=True, default=0)

    #owner_id = Column(Integer, ForeignKey("inventory.id"))

    #owner = relationship("Inventory", back_populates="items")


