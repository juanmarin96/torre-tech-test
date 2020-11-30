from typing import Optional

from pydantic import BaseModel

import datetime

# Shared properties
class PostBase(BaseModel):
    user: str
    user_image: Optional[str] = None
    content: str
    image: Optional[str] = None


# Properties to receive on Post creation
class PostCreate(PostBase):
    pass


# Properties to receive on Post update
class PostUpdate(PostBase):
    pass


# Properties shared by models stored in DB
class PostInDBBase(PostBase):
    id: int
    created_at: datetime.datetime

    class Config:
        orm_mode = True


# Properties to return to client
class Post(PostInDBBase):
    pass


# Properties properties stored in DB
class PostInDB(PostInDBBase):
    pass
