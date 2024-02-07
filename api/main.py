from fastapi import FastAPI, status, HTTPException, Depends
import schemas
import models
from database import engine, Base, session_local
from sqlalchemy.orm import Session
from typing import List

# Create the database tables if they do not exist
Base.metadata.create_all(engine)

# Create a FastAPI instance
app = FastAPI()


def get_db():
    """
    Instantiates a new session for each request and closes it after the request is done
    Used as a dependency for the routes
    """
    db = session_local()
    try:
        yield db
    finally:
        db.close()


@app.get("/", response_model=List[schemas.TodoBase])
async def list_item(session: Session = Depends(get_db)):
    """
    Returns a list of all todos
    """
    # session = Session(bind=engine, expire_on_commit=False)
    # todos = session.query(models.Todo).all()
    # session.close()
    todos = session.query(models.Todo).all()

    if not todos:
        raise HTTPException(status_code=404, detail="No todos found")
    return todos


@app.post(
    "/item/", response_model=schemas.TodoBase, status_code=status.HTTP_201_CREATED
)
async def create_item(item: schemas.TodoBase, session: Session = Depends(get_db)):
    """
    Creates a new todo
    """
    # session = Session(bind=engine, expire_on_commit=False)

    todo = models.Todo(**item.dict())
    session.add(todo)
    session.commit()
    session.refresh(todo)
    # session.close()

    return todo


@app.get("/item/{id}", response_model=schemas.TodoBase, status_code=status.HTTP_200_OK)
async def read_item(id: int, session: Session = Depends(get_db)):
    """
    Returns a single todo
    """
    # session = Session(bind=engine, expire_on_commit=False)
    todo = session.query(models.Todo).get(id)
    # session.close()

    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    return todo


@app.put("/item/{id}", response_model=schemas.TodoBase, status_code=status.HTTP_200_OK)
async def update_item(
    id: int, item: schemas.TodoBase, session: Session = Depends(get_db)
):
    """
    Returns a single todo
    """
    # session = Session(bind=engine, expire_on_commit=False)
    todo = session.query(models.Todo).get(id)

    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")

    for var, value in item.dict().items():
        setattr(todo, var, value)

    session.commit()
    # session.close()
    return todo


@app.delete("/item/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_item(id: int, session: Session = Depends(get_db)):
    """
    Deletes a single todo
    """
    # session = Session(bind=engine, expire_on_commit=False)
    todo = session.query(models.Todo).get(id)

    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")

    session.delete(todo)
    session.commit()
    # session.close()
    return {"detail": "Todo deleted successfully"}
