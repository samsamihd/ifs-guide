from datetime import datetime
from typing import Dict, Optional
from uuid import UUID
from pydantic import BaseModel


# Messages pydantic model

class MessageBase(BaseModel):
    id: UUID | None = None
    role: str
    content: str
    created_at: datetime | None = None


class MessageCreate(MessageBase):
    pass


class Message(MessageBase):
    interaction_id: UUID

    class Config:
        from_attributes = True


# Interactions pydantic model

class InteractionBase(BaseModel):
    id: UUID | None = None
    settings: Optional[Dict]
    created_at: datetime | None = None
    updated_at: datetime | None = None


class InteractionCreate(InteractionBase):
    pass


class Interaction(InteractionBase):
    messages: list[Message] = []

    class Config:
        from_attributes = True
