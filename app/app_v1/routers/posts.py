from fastapi import Response, status, HTTPException, APIRouter, Depends
from app.db.schemas import PostResponse, CreatePostRequest, UpdatePostRequest
from app.db import models
from app.db.database import get_db
from sqlalchemy.orm import Session
from typing import List

router = APIRouter(
    prefix='/api'
)

# GET: /api/posts
@router.get('/posts', response_model=List[PostResponse])
async def get_all_posts(db: Session = Depends(get_db)):
    all_posts = db.query(models.Post).all()
    return all_posts

# GET: /api/posts/5
@router.get('/posts/{id}', response_model=PostResponse)
async def get_post_by_id(id: int, db: Session = Depends(get_db)):
    post = db.query(models.Post).filter(models.Post.id == id).first()
    # check if post is null
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'post with id: {id} not found!')
    return post

# POST: /api/posts
@router.post('/posts', status_code=status.HTTP_201_CREATED, response_model=PostResponse)
async def create_post(post: CreatePostRequest, db: Session = Depends(get_db)):
     # new_post = models.Post(title=post.title, content=post.content, 
    #     published=post.published)
    new_post = models.Post(**post.dict())
    db.add(new_post)
    db.commit()
    db.refresh(new_post) #returns the created obj with id field
    return new_post

# DELETE: /api/posts/5
@router.delete('/posts/{id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_post(id: int, db: Session = Depends(get_db)):
    # Create the query
    post_query = db.query(models.Post).filter(models.Post.id == id)

    # Run the query by calling .first()
    if post_query.first() == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'post with id: {id} does not exist')

    # Delete the item
    post_query.delete()
    db.commit()

    return Response(status_code=status.HTTP_204_NO_CONTENT)

# PUT: /api/posts/5
@router.put('/posts/{id}', response_model=PostResponse)
async def update_post(id: int, post: UpdatePostRequest, db: Session = Depends(get_db)):
    # Create the query
    post_query = db.query(models.Post).filter(models.Post.id == id)

    # Run the query by calling .first()
    if post_query.first() == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'post with id: {id} does not exist')

    post_query.update(post.dict())
    db.commit()
    return post_query.first()