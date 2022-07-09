from __future__ import annotations
from typing import Union, Optional
from pydantic import BaseModel



class ItemBase(BaseModel):
    name: str
    quantity: Union[int, None] = None



class ItemCreate(ItemBase):
    name: str


class ItemUpdate(ItemBase):
    name: Optional[str] = None
    quantity: Optional[int] = None

    
    
class Item(ItemBase):
    id: int
    

    class Config:
        orm_mode = True

"""
class InventoryBase(BaseModel):
    category: str

class InventoryCreate(InventoryBase):
    category: str
    
class InventoryUpdate(InventoryBase):
    pass

class Inventory(InventoryBase):
    id: int
    items: List[Item] = []

    class Config:
        orm_mode = True
"""