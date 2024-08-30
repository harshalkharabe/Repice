from typing import Optional
from pydantic import BaseModel, EmailStr
from sqlalchemy.dialects.postgresql import UUID
from src.db_session import Base
import uuid
from sqlalchemy import  Column, Integer, String, Boolean, MetaData, DateTime

class User(Base):
    __tablename__ = "user"

    id = Column("id", UUID(as_uuid=True), default=uuid.uuid4, primary_key=True, index=True)
    username = Column(String)
    firstname = Column(String)
    lastname = Column(String)
    email = Column(String)
    phone_no = Column(String)
    password = Column(String)
    is_logged_in = Column(Boolean)

class User_v2(BaseModel):
    id: Optional[uuid.UUID] = None
    username: str
    firstname: str
    lastname: str
    email: EmailStr
    phone_no: str
    password: str
    is_logged_in: bool
    
    