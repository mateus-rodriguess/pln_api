from email import message
from sqlalchemy.orm import Session
from apps.models.accuracy_models import AccuracyModel
from apps.schemas import accuracy_schema
from apps.pln.accuracy import accuracy_response

def add_accuracy(db: Session, accuracy_data: accuracy_schema.AccuracyResponse):
    """
    Save accuracy
    """

    accuracy =  accuracy_response(text=accuracy_data.message)
    print(accuracy)
    db_accuracy = AccuracyModel(
        accuracy= float(accuracy),
        message=accuracy_data.message)
    
    db.add(db_accuracy)
    db.commit()
    db.refresh(db_accuracy)

    return db_accuracy

def list_accuracy(db: Session):
    return db.query(AccuracyModel).filter().all()