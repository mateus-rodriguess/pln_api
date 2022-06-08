from datetime import timedelta
from typing import List

from apps.crud import user_crud
from apps.database import get_db
from apps.schemas.user_schemas import UserCreateSchema, UserSchema
from apps.services.security import (ACCESS_TOKEN_EXPIRE_MINUTES,
                                    authenticate_user, create_access_token,
                                    get_current_active_user, get_current_user)
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from starlette.status import HTTP_401_UNAUTHORIZED
from apps.services.username_validation import validation

router = APIRouter()


@router.get("", response_model=List[UserSchema])
async def users(db: Session = Depends(get_db)):
    """
    Get users
    """
    users = user_crud.get_all_users(db)
    return list(users)


@router.get("/{username:str}", response_model=UserSchema)
async def get_user(username: str, db: Session = Depends(get_db)) -> UserSchema:
    user = user_crud.get_user_by_username(db, username)
    if user:
        print(user)
        return user
    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User no exist",
        )



@router.post("/login")
async def login_for_access_token(db: Session = Depends(get_db), form_data: OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )

    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}


@router.post("/register", response_model=UserSchema)
async def sign_up(user_data: UserCreateSchema, db: Session = Depends(get_db)):
    user = user_crud.get_user_by_username(db, user_data.username)
    if user:
        raise HTTPException(
            status_code=409,
            detail="username no exist",
        )

    user_data.username = validation(user_data.username)
    new_user = user_crud.add_user(db, user_data)
    return new_user


# @router.get("/me", response_model=UserSchema)
# async def read_users_me(current_user: UserSchema = Depends(get_current_active_user)):
#     return current_user
