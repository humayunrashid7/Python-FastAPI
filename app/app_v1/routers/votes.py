from fastapi import Response, status, HTTPException, APIRouter, Depends
from app.db.schemas import CreateVoteRequest
from app.db import models
from app.db.database import get_db
from sqlalchemy.orm import Session
from typing import List, Optional
from app.auth import oauth2

router = APIRouter(
    prefix='/api'
)

# POST: /api/votes
@router.post('/votes', status_code=status.HTTP_201_CREATED)
async def create_vote(req: CreateVoteRequest, db: Session = Depends(get_db), 
    current_user: models.User = Depends(oauth2.get_current_user)):
    # check if post already exists
    post_exists = db.query(models.Post).filter(models.Post.id == req.post_id).first()
    if not post_exists:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
            detail=f'The post id: {req.post_id} does not exist.')

    vote_query = db.query(models.Vote).filter(
        models.Vote.post_id == req.post_id,
        models.Vote.user_id == current_user.id
    )
    vote_exists = vote_query.first()
    if (req.dir == 1): # if up-voted or liked a post
        if vote_exists:
            raise HTTPException(status_code=status.HTTP_409_CONFLICT,
                detail=f'user id: {current_user.id} has alread voted on post: {req.post_id}')
        # If vote doesn't exist: add vote
        new_vote = models.Vote(post_id = req.post_id, user_id = current_user.id)
        db.add(new_vote)
        db.commit()
        return {'message': 'successfully added vote'}
    else: # if down-voted or disliked (means vote already exists and user had liked it)
        if not vote_exists:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                detail='vote does not exist')
        # if vote exists, delete it as user has requested to remove vote or disliked it
        vote_query.delete()
        db.commit()
        return {'message': 'successfully deleted vote'}