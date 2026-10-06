from fastapi import FastAPI, Depends, HTTPException
from pydantic import BaseModel
from schemas import PostBase, PostResponse,CreatePost
from database import get_db
from sqlalchemy.orm import Session
from models import Post
from database import Base, engine

app = FastAPI()

Base.metadata.create_all(bind=engine)

@app.post('/posts', response_model=PostResponse)
def create_post(post : CreatePost, db: Session = Depends(get_db)):
    new_post =  Post(
        title = post.title,
        content = post.content,
        published = post.published
    )

    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post



@app.get("/posts", response_model=list[PostResponse])
def get_posts(
    db: Session = Depends(get_db)
):
    posts = db.query(Post).all()

    return posts

@app.get("/posts/{post_id}", response_model=PostResponse)
def get_post(
    post_id: int,
    db: Session = Depends(get_db)
):
    post = db.query(Post).filter(Post.id == post_id).first()

    if post is None:
        raise HTTPException(
            status_code=404,
            detail="Post not found"
        )

    return post

