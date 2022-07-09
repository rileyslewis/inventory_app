from typing import Any, List
from fastapi import Depends, FastAPI, HTTPException
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from .sql_app import crud, schemas, models
from .sql_app.database import *
import uvicorn
from fastapi.middleware.cors import CORSMiddleware



models.Base.metadata.create_all(bind=engine)

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


#### ---- Item Routes ---- ####

@app.get("/", response_model=List[schemas.Item])
def read_items(db: Session = Depends(get_db),
               skip: int = 0, limit: int = 100, ) -> Any:
    items = crud.item.get_all(db, skip=skip, limit=limit)
    try:
        return items
    except:
        raise HTTPException(status_code=404, detail="Items Could not be found.")


@app.post("/", response_model=schemas.Item)
def create_item(*, db:Session = Depends(get_db), item_inside: schemas.ItemCreate) -> Any:
    item = crud.item.create_with_category(db=db, object_inside=item_inside)
    try:
        return item
    except:
        raise HTTPException(status_code=422, detail="Unable to Process Creation Request..")


@app.put("/{id}", response_model=schemas.Item)
def update_item(*, db: Session = Depends(get_db), id: int, item_inside: schemas.ItemUpdate, ) -> Any:
    item = crud.item.get(db=db, id=id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    item = crud.item.update(db=db, db_object=item, object_inside=item_inside)
    return item


@app.get("/{id}", response_model=schemas.Item)
def read_item(*, db: Session = Depends(get_db), id: int, ) -> Any:
    item = crud.item.get(db=db, id=id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return item

@app.delete("/{id}", response_model=schemas.Item)
def delete_target(*, db: Session = Depends(get_db), id: int, ) -> Any:
    item = crud.item.get(db=db, id=id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    item = crud.item.delete_target(db=db, id=id)
    return JSONResponse(status_code =200, content = {"message": "Item Deleted Successfully"})


#### ---- Item Routes end ---- ####

