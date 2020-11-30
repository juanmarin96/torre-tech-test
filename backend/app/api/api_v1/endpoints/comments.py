from typing import Any, List

from fastapi import APIRouter, Body, Depends, HTTPException
from fastapi.encoders import jsonable_encoder
from pydantic.networks import EmailStr
from sqlalchemy.orm import Session

import crud
import models
import schemas
from api import deps
from core.config import settings
import uuid

router = APIRouter()

Comment_PHOTO_EXT = '.jpeg'


@router.get("/", response_model=List[schemas.Comment])
def read_Comments(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
    current_Comment: models.Comment = Depends(deps.get_current_active_superComment),
) -> Any:
    """
    Retrieve Comments.
    """
    Comments = crud.Comment.get_multi(db, skip=skip, limit=limit)
    return Comments


@router.post("/", response_model=schemas.Comment)
def create_Comment(
    *,
    db: Session = Depends(deps.get_db),
    Comment_in: schemas.CommentCreate,
    current_Comment: models.Comment = Depends(deps.get_current_active_superComment),
) -> Any:
    """
    Create new Comment.
    """
    Comment = crud.Comment.get_by_email(db, email=Comment_in.email)
    if Comment:
        raise HTTPException(
            status_code=400,
            detail="The Comment with this Commentname already exists in the system.",
        )
    Comment = crud.Comment.create(db, obj_in=Comment_in)
    
    return Comment


@router.put("/me", response_model=schemas.Comment)
def update_Comment_me(
    *,
    db: Session = Depends(deps.get_db),
    password: str = Body(None),
    full_name: str = Body(None),
    email: EmailStr = Body(None),
    current_Comment: models.Comment = Depends(deps.get_current_active_Comment),
) -> Any:
    """
    Update own Comment.
    """
    current_Comment_data = jsonable_encoder(current_Comment)
    Comment_in = schemas.CommentUpdate(**current_Comment_data)
    if password is not None:
        Comment_in.password = password
    if full_name is not None:
        Comment_in.full_name = full_name
    if email is not None:
        Comment_in.email = email
    Comment = crud.Comment.update(db, db_obj=current_Comment, obj_in=Comment_in)
    return Comment


@router.get("/me", response_model=schemas.Comment)
def read_Comment_me(
    db: Session = Depends(deps.get_db),
    current_Comment: models.Comment = Depends(deps.get_current_active_Comment),
) -> Any:
    """
    Get current Comment.
    """
    return current_Comment


@router.get("/{Comment_id}", response_model=schemas.Comment)
def read_Comment_by_id(
    Comment_id: int,
    current_Comment: models.Comment = Depends(deps.get_current_active_Comment),
    db: Session = Depends(deps.get_db),
) -> Any:
    """
    Get a specific Comment by id.
    """
    Comment = crud.Comment.get(db, id=Comment_id)
    if Comment == current_Comment:
        return Comment
    if not crud.Comment.is_superComment(current_Comment):
        raise HTTPException(
            status_code=400, detail="The Comment doesn't have enough privileges"
        )
    return Comment


@router.put("/{Comment_id}", response_model=schemas.Comment)
def update_Comment(
    *,
    db: Session = Depends(deps.get_db),
    Comment_id: int,
    Comment_in: schemas.CommentUpdate,
    current_Comment: models.Comment = Depends(deps.get_current_active_superComment),
) -> Any:
    """
    Update a Comment.
    """
    Comment = crud.Comment.get(db, id=Comment_id)
    if not Comment:
        raise HTTPException(
            status_code=404,
            detail="The Comment with this Commentname does not exist in the system",
        )
    Comment = crud.Comment.update(db, db_obj=Comment, obj_in=Comment_in)
    return Comment
