from typing import Any, Dict, List, Optional, Type, Generic, TypeVar, Union
from http.client import HTTPException
from sqlalchemy.orm import Session
from . import models, schemas
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel
from sqlalchemy.ext.declarative import as_declarative, declared_attr




@as_declarative()
class Vanilla:
    id: Any
    __name__: str
    @declared_attr
    def __tablename__(cls) -> str:
        return cls.__name__.lower()


ModelType = TypeVar("ModelType", bound=Vanilla)
CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseModel)
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=BaseModel)

class CRUDVanilla(Generic[ModelType, CreateSchemaType, UpdateSchemaType]):
    def __init__(self, model: Type[ModelType]):
        self.model = model
        
    def get(self, db: Session, id: Any) -> Optional[ModelType]:
        return db.query(self.model).filter(self.model.id == id).first()
    
    def get_all(self, db: Session, *, skip: int = 0, limit: int = 100) -> List[ModelType]:
        return db.query(self.model).offset(skip).limit(limit).all()
    
    def create(self, db: Session, *, object_inside: CreateSchemaType) -> ModelType:
        object_in_data = jsonable_encoder(object_inside)
        db_object = self.model(**object_in_data)
        db.add(db_object)
        db.commit()
        db.refresh(db_object)
        return db_object
    
    def update(self, db: Session, *, db_object: ModelType, object_inside: Union[UpdateSchemaType, Dict[str, Any]]) -> ModelType:
        object_data = jsonable_encoder(db_object)
        if isinstance(object_inside, dict):
            update_data = object_inside
        else:
            update_data = object_inside.dict(exclude_unset=True)
        for field in object_data:
            if field in update_data:
                setattr(db_object, field, update_data[field])
        db.add(db_object)
        db.commit()
        db.refresh(db_object)
        return db_object
    
    def delete_target(self, db: Session, *, id: int) -> ModelType:
        _object = db.query(self.model).get(id)
        db.delete(_object)
        db.commit()
        return _object



class CRUDItem(CRUDVanilla[models.Item, schemas.ItemCreate, schemas.ItemUpdate]):
    def create_with_category(self, db: Session, *, object_inside: schemas.ItemCreate) -> models.Item:
        object_in_data = jsonable_encoder(object_inside)
        db_object = self.model(**object_in_data)
        db.add(db_object)
        db.commit()
        db.refresh(db_object)
        return db_object
    
    def get_all_by_category(self, db: Session, *, id: int, skip: int = 0, limit: int = 100) -> List[models.Item]:
        return db.query(self.model).filter(models.Item.id == id).offset(skip).limit(limit).all()
    

        
item = CRUDItem(models.Item)
#inventory = CRUDInventory(models.Inventory)