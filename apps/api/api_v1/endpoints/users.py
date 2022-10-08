from typing import List

from apps.crud import user_crud
from apps.api.api_v1.deps import get_db
from apps.schemas.user_schemas import UserResponseSchema
from fastapi import (APIRouter, Depends, HTTPException, Request, Response,
                     status)
from sqlalchemy.orm import Session
from starlette.status import HTTP_401_UNAUTHORIZED
from fastapi_redis_cache import FastApiRedisCache, cache
from apps.core.config import get_settings
from apps.core.security import get_current_user_is_admin
settings = get_settings()

router = APIRouter()

LOCAL_REDIS_URL = settings.LOCAL_REDIS_URL


@router.on_event("startup")
def startup():
    redis_cache = FastApiRedisCache()
    redis_cache.init(
        host_url=LOCAL_REDIS_URL,
        prefix="api-pln-cache",
        response_header="X-api-pln-Cache",
        ignore_arg_types=[Request, Response, Session]
    )


@router.get("/", response_model=List[UserResponseSchema])
@cache()
async def users(limit: int = 10, db: Session = Depends(get_db), current_user=Depends(get_current_user_is_admin)):
    """
    Get users
    """
    users = user_crud.get_all_users(db=db, limit=limit)
    return list(users)


@router.get("/{username:str}", response_model=UserResponseSchema)
@cache()
async def get_user(username: str, db: Session = Depends(get_db)):
    user = user_crud.get_user_by_username(db, username)
    if user:
        return user
    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User no exist",
        )
