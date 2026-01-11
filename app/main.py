from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session
from pydantic import BaseModel
from typing import List

from app import models
from app.database import engine, SessionLocal

from sqlalchemy.exc import OperationalError
import time

for _ in range(10):
    try:
        models.Base.metadata.create_all(bind=engine)
        break
    except OperationalError:
        time.sleep(2)


app = FastAPI()


# --------------------
# Pydantic Schemas
# --------------------

class PostCreate(BaseModel):
    title: str
    content: str
    published: bool = True


class PostResponse(PostCreate):
    id: int

    class Config:
        orm_mode = True


# --------------------
# Database Dependency
# --------------------

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# --------------------
# Routes
# --------------------

@app.get("/")
def root():
    return {"message": "Hello World"}


@app.get("/post", response_model=List[PostResponse])
def get_posts(db: Session = Depends(get_db)):
    return db.query(models.Post).all()


@app.post("/post", status_code=status.HTTP_201_CREATED, response_model=PostResponse)
def create_post(post: PostCreate, db: Session = Depends(get_db)):
    new_post = models.Post(**post.dict())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post


@app.get("/post/{id}", response_model=PostResponse)
def get_post(id: int, db: Session = Depends(get_db)):
    post = db.query(models.Post).filter(models.Post.id == id).first()
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")
    return post


@app.delete("/post/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int, db: Session = Depends(get_db)):
    post = db.query(models.Post).filter(models.Post.id == id).first()
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")

    db.delete(post)
    db.commit()


@app.put("/post/{id}", response_model=PostResponse)
def update_post(id: int, post: PostCreate, db: Session = Depends(get_db)):
    db_post = db.query(models.Post).filter(models.Post.id == id).first()
    if not db_post:
        raise HTTPException(status_code=404, detail="Post not found")

    for key, value in post.dict().items():
        setattr(db_post, key, value)

    db.commit()
    db.refresh(db_post)
    return db_post
