from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

import crud
import models
import schemas
from api import deps

router = APIRouter()


@router.get("/", response_model=List[schemas.Post])
def read_Posts(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
    current_Comment: models.Comment = Depends(deps.get_current_active_Comment),
) -> Any:
    """
    Retrieve Posts.
    """
    if crud.Comment.is_superComment(current_Comment):
        Posts = crud.Post.get_multi(db, skip=skip, limit=limit)
    else:
        Posts = crud.Post.get_multi_by_owner(
            db=db, owner_id=current_Comment.id, skip=skip, limit=limit
        )
    return Posts


@router.post("/", response_model=schemas.Post)
def create_Post(
    *,
    db: Session = Depends(deps.get_db),
    Post_in: schemas.PostCreate,
    current_Comment: models.Comment = Depends(deps.get_current_active_Comment),
) -> Any:
    """
    Create new Post.
    """
    Post = crud.Post.create_with_owner(db=db, obj_in=Post_in, owner_id=current_Comment.id)
    return Post


@router.put("/{id}", response_model=schemas.Post)
def update_Post(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    Post_in: schemas.PostUpdate,
    current_Comment: models.Comment = Depends(deps.get_current_active_Comment),
) -> Any:
    """
    Update an Post.
    """
    Post = crud.Post.get(db=db, id=id)
    if not Post:
        raise HTTPException(status_code=404, detail="Post not found")
    if not crud.Comment.is_superComment(current_Comment) and (Post.owner_id != current_Comment.id):
        raise HTTPException(status_code=400, detail="Not enough permissions")
    Post = crud.Post.update(db=db, db_obj=Post, obj_in=Post_in)
    return Post


@router.get("/{id}", response_model=schemas.Post)
def read_Post(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    current_Comment: models.Comment = Depends(deps.get_current_active_Comment),
) -> Any:
    """
    Get Post by ID.
    """
    Post = crud.Post.get(db=db, id=id)
    if not Post:
        raise HTTPException(status_code=404, detail="Post not found")
    if not crud.Comment.is_superComment(current_Comment) and (Post.owner_id != current_Comment.id):
        raise HTTPException(status_code=400, detail="Not enough permissions")
    return Post


@router.delete("/{id}", response_model=schemas.Post)
def delete_Post(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    current_Comment: models.Comment = Depends(deps.get_current_active_Comment),
) -> Any:
    """
    Delete an Post.
    """
    Post = crud.Post.get(db=db, id=id)
    if not Post:
        raise HTTPException(status_code=404, detail="Post not found")
    if not crud.Comment.is_superComment(current_Comment) and (Post.owner_id != current_Comment.id):
        raise HTTPException(status_code=400, detail="Not enough permissions")
    Post = crud.Post.remove(db=db, id=id)
    return Post
