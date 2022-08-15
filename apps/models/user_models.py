import uuid
from datetime import datetime

from apps.database import Base
from sqlalchemy import Boolean, Column, DateTime, Integer, String


def generate_uuid():
    return str(uuid.uuid4())


class UserModel(Base):
    __tablename__ = "users"
    id = Column(String, default=generate_uuid,
                primary_key=True, index=True, nullable=False)

    username = Column(String(20), unique=True, index=True, nullable=False)
    first_name = Column(String(40), nullable=False)
    last_name = Column(String(40), nullable=False)
    email = Column(String(150), unique=True, index=True, nullable=False)
    hashed_password = Column(String)

    is_active = Column(Boolean, default=True)
    is_admin = Column(Boolean, default=False)

    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)

    def full_name(self):
        return self.first_name + " " + self.last_name
