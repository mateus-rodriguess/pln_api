from email import message
from sqlalchemy.orm import Session
from apps.models.accuracy_models import AccuracyModel
from apps.schemas import accuracy_schema
from apps.schemas.accuracy_schema import AccuracyResponse
from apps.pln.accuracy import accuracy_predict


def add_accuracy(db: Session, accuracy_data: accuracy_schema.Accuracy):
    """
    Save accuracy
    """
    accuracy = accuracy_predict(text=accuracy_data.message)

    if not accuracy_data.save:
        AccuracyResponse.message=accuracy_data.message
        AccuracyResponse.accuracy=accuracy

        return AccuracyResponse
    else:
        db_accuracy=AccuracyModel(
            accuracy = accuracy, message = accuracy_data.message)
        db.add(db_accuracy)
        db.commit()
        db.refresh(db_accuracy)
        return db_accuracy


def list_accuracy(db: Session, limit: int):
    return db.query(AccuracyModel).filter().limit(limit)
