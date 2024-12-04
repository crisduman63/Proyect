from fastapi import APIRouter, Depends
from app.schemas import UserCreate, User
from app.crud import create_user, get_users
from app.database import SessionLocal

router = APIRouter()

@router.post("/users/", response_model=User)
async def create_new_user(user: UserCreate, db: Session = Depends(get_db)):
    return await create_user(db=db, user_create=user)

@router.get("/users/", response_model=List[User])
async def get_users_list(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return await get_users(db=db, skip=skip, limit=limit)
