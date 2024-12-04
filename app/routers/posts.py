from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from ..database import get_db
from ..models import Post
from ..schemas import PostCreate, PostOut
from ..crud import create_post, get_posts

router = APIRouter()

@router.post("/posts", response_model=PostOut)
async def create_post(post: PostCreate, db: AsyncSession = Depends(get_db)):
    return await create_post(db, post)

@router.get("/posts", response_model=List[PostOut])
async def read_posts(skip: int = 0, limit: int = 10, db: AsyncSession = Depends(get_db)):
    return await get_posts(db, skip, limit)
