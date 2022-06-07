from datetime import datetime
from email import message
from pyparsing import col
from sqlalchemy import Column, Float, Integer, String, Boolean, DateTime, column

from apps.database import Base

class AccuracyModel(Base):
    __tablename__ = 'accuracys'
    id = Column(Integer, primary_key=True, index=True)

    accuracy = Column(Float)
    message = Column(String)
    
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)