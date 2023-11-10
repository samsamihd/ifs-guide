import uuid
from sqlalchemy import Column, ForeignKey, String, DateTime, JSON
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from app.database import Base


class Interaction(Base):
    __tablename__ = "interactions"

    id = Column(String(36), primary_key=True,
                default=lambda: str(uuid.uuid4()))
    settings = Column(JSON)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, onupdate=func.now())

    messages = relationship("Message", back_populates="interaction")


class Message(Base):
    __tablename__ = "messages"

    id = Column(String(36), primary_key=True,
                default=lambda: str(uuid.uuid4()))
    role = Column(String)
    content = Column(String)
    interaction_id = Column(String, ForeignKey("interactions.id"))
    created_at = Column(DateTime, server_default=func.now())

    interaction = relationship("Interaction", back_populates="messages")
