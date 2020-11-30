from typing import Optional

from pydantic import BaseModel, EmailStr, AnyHttpUrl, Json

import datetime

# Shared properties
class CommentBase(BaseModel):
    post_id: int
    user: str
    user_image: Optional[str]
    content: str



# Properties to receive via API on creation
class CommentCreate(CommentBase):
    pass


# Properties to receive via API on update
class CommentUpdate(CommentBase):
    pass

class CommentInDBBase(CommentBase):
    id: int = None
    created_at: datetime.datetime

    class Config:
        orm_mode = True


# Additional properties to return via API
class Comment(CommentInDBBase):
    pass


# Additional properties stored in DB
class CommentInDB(CommentInDBBase):
    pass
