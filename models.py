from sqlalchemy import Column, Integer, String
from database import Base

class Item(Base):
    __tablename__ = "items"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100))  # Added length for Supabase compatibility
    description = Column(String(500), nullable=True)