from fastapi import Depends, APIRouter, HTTPException
from sqlalchemy.orm import Session

from app.schemas import Interaction, InteractionCreate, Message, MessageCreate
from app.services import get_db, create_interaction, get_interactions, get_messages, create_message

router = APIRouter()


@router.get("/")
def read_root():
    return "This is IFS Guide!"


@router.post("/interactions/", response_model=InteractionCreate)
def create_interaction_router(interaction: Interaction, db: Session = Depends(get_db)):
    return create_interaction(db=db, interaction=interaction)


@router.get("/interactions/", response_model=list[Interaction])
def get_interactions_router(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    interactions = get_interactions(db, skip=skip, limit=limit)
    return interactions


@router.get("/interactions/{interaction_id}", response_model=list[Message])
def get_messages_router(interaction_id: str, db=Depends(get_db)):
    messages = get_messages(db, interaction_id)
    if not messages:
        raise HTTPException(status_code=404, detail="Interaction not found")
    return messages


@router.post("/interactions/{interaction_id}/messages", response_model=MessageCreate)
def create_message_router(interaction_id: str, message: MessageCreate, db=Depends(get_db)):
    message = create_message(db, message, interaction_id)
    if not message:
        raise HTTPException(status_code=404, detail="Interaction not found")
    return message
