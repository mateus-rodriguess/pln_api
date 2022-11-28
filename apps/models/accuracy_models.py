from datetime import datetime
from sqlalchemy import Column, Float, Integer, String, Boolean, DateTime, column
from sqlalchemy.dialects.postgresql import UUID
from apps.db.database import Base
import uuid
from sqlalchemy.dialects.postgresql import UUID


class AccuracyModel(Base):
    __tablename__ = 'accuracys'
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)

    accuracy = Column(Float)
    message = Column(String)

    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)
