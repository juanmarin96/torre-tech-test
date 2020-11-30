from typing import TYPE_CHECKING

from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship

from database.base_class import Base

if TYPE_CHECKING:
    from .post import Post  # noqa: F401

import datetime

class Comment(Base):
    id = Column(Integer, primary_key=True, index=True)
    user = Column(String)
    content = Column(String)
    post_id = Column(Integer, ForeignKey('post.id'))
    post = relationship("Post", back_populates="comments")
    created_at = Column(DateTime, default=datetime.datetime.utcnow)