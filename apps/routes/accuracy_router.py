from typing import List

from apps.crud import accuracy_crud
from apps.database import get_db
from apps.schemas import accuracy_schema
from apps.services.security import get_current_user_is_admin
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session


router = APIRouter()


@router.post("/accuracy", status_code=status.HTTP_200_OK,response_model=accuracy_schema.AccuracyResponse)
async def accuracy(accuracy_resquest: accuracy_schema.Accuracy, db: Session = Depends(get_db)):
    """
    Accuracy
    """
    accuracy = accuracy_crud.add_accuracy(db, accuracy_resquest)

    return accuracy


@router.get("/", response_model=List[accuracy_schema.AccuracyResponse], status_code=status.HTTP_200_OK)
async def home(db: Session = Depends(get_db), current_user=Depends(get_current_user_is_admin)):
    """
    Home
    """
    accuracys = accuracy_crud.list_accuracy(db)
    return list(accuracys)
