import uuid
from src.db_session import Base
from sqlalchemy.dialects.postgresql import UUID
from pydantic import BaseModel, UUID4, Field
from typing import List, Optional
from datetime import datetime
from sqlalchemy import  Column, Integer, String, Boolean, MetaData, DateTime,ForeignKey,Text

class RecipeBase(BaseModel):
    id: Optional[uuid.UUID] = None    
    user_id: UUID4
    title: str = Field(..., max_length=255, description="Title of the recipe")
    description: Optional[str] = Field(None, description="Description of the recipe")
    ingredients: List[str] = Field(..., description="List of ingredients")
    # instructions: str = Field(..., description="Cooking instructions")
    category: Optional[str] = Field(None, max_length=100, description="Recipe category (e.g., Dessert, Main Course)")
    # image: Optional[str] = Field(None, description="URL or path to an image of the recipe")
    created_at: datetime

class Recipe(Base):
    __tablename__ = "recipes"

    id = Column("id", UUID(as_uuid=True), default=uuid.uuid4, primary_key=True, index=True)
    title = Column(String(255), nullable=False)  # Recipe title
    description = Column(Text, nullable=True)  # Recipe description
    ingredients = Column(Text, nullable=False)  # List of ingredients (could be stored as JSON or comma-separated string)
    category = Column(String(100), nullable=True)  # Recipe category (e.g., Dessert)
    user_id = Column(UUID(as_uuid=True), ForeignKey('user.id', ondelete='CASCADE'), nullable=False)  # User who created the recipe
    # image = Column(Text, nullable=True)  # URL or path to the recipe image
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)  # Timestamp of recipe creation

