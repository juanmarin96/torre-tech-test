from models import post
from api.api_v1.endpoints import comments
from fastapi import APIRouter

from api.api_v1.endpoints import posts, comments

api_router = APIRouter()
api_router.include_router(comments.router, prefix="/posts", tags=["posts"])
api_router.include_router(posts.router, prefix="/comments", tags=["comments"])
