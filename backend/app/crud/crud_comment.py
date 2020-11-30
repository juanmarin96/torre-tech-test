from typing import Optional, List

from sqlalchemy.orm import Session

from crud.base import CRUDBase
from models.comment import Comment
from schemas.comment import CommentCreate, CommentUpdate


class CRUDComment(CRUDBase[Comment, CommentCreate, CommentUpdate]):

    def get_by_post(self, db: Session, *, post_id: str) -> Optional[List[Comment]]:
        return db.query(Comment).filter(Comment.post_id == post_id).all()

    


comment = CRUDComment(Comment)
