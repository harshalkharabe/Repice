from typing import Optional
from pydantic import BaseModel, EmailStr
from uuid import UUID
import uuid
from sqlalchemy import  Column, Integer, String, Boolean, MetaData, DateTime

# class User(Base):
#     __tablename__ = "user"

#     id = Column(uuid(as_uuid=True), primary_key=True, index=True)
#     username = Column(String)
#     firstname = Column(String)
#     lastname = Column(String)
#     email = Column(String)
#     phone_no = Column(String)
#     password = Column(String)
#     is_logged_in = Column(String)

class User_v2(BaseModel):
    id: Optional[UUID]=None
    username: str
    firstname: str
    lastname: str
    email: EmailStr
    phone_no: str
    password: str
    is_logged_in: Optional[str] = None
    
    