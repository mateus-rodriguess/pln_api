from typing import List

from apps.crud import user_crud
from apps.database import get_db
from apps.schemas.user_schemas import UserResponseSchema
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from starlette.status import HTTP_401_UNAUTHORIZED

router = APIRouter()


@router.get("/", response_model=List[UserResponseSchema])
async def users(db: Session = Depends(get_db)):
    """
    Get users
    """
    users = user_crud.get_all_users(db)
    return list(users)


@router.get("/{username:str}", response_model=UserResponseSchema)
async def get_user(username: str, db: Session = Depends(get_db)):
    user = user_crud.get_user_by_username(db, username)
    if user:
        print(user)
        return user
    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User no exist",
        )

