from email import message
from sqlalchemy.orm import Session
from apps.models.accuracy_models import AccuracyModel
from apps.schemas import accuracy_schema
from apps.pln.accuracy import accuracy_response
from apps.services.translate_message import translate

def add_accuracy(db: Session, accuracy_data: accuracy_schema.AccuracyResponse):
    """
    Save accuracy
    """
    message = translate(accuracy_data.message)
    accuracy =  accuracy_response(text=message)
    
    db_accuracy = AccuracyModel(accuracy=accuracy, message=message)
    
    db.add(db_accuracy)
    db.commit()
    db.refresh(db_accuracy)
    return db_accuracy

def list_accuracy(db: Session):
    return db.query(AccuracyModel).filter().all()