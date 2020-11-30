from typing import TYPE_CHECKING

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.sql.sqltypes import DateTime

from database.base_class import Base

if TYPE_CHECKING:
    from .comment import Comment  # noqa: F401

import datetime


class Post(Base):
    id = Column(Integer, primary_key=True, index=True)
    user = Column(String, index=True)
    user_image = Column(String, nullable=True)
    content = Column(String)
    image = Column(String, nullable=True)
    comments = relationship("Comment", back_populates="Post")
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
