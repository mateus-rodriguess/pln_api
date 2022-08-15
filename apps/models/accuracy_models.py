from datetime import datetime
from sqlalchemy import Column, Float, Integer, String, Boolean, DateTime, column

from apps.database import Base


def generate_uuid():
    return str(uuid.uuid4())


class AccuracyModel(Base):
    __tablename__ = 'accuracys'
    id = Column(String, default=generate_uuid,
                primary_key=True, index=True, nullable=False)

    accuracy = Column(Float)
    message = Column(String)

    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)
