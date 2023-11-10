from uuid import UUID
from sqlalchemy.orm import Session
import g4f

from app.models import Interaction, Message
from app.schemas import InteractionCreate, MessageCreate
from app.database import SessionLocal


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def create_interaction(db: Session, interaction: InteractionCreate):
    interaction = Interaction(settings=interaction.settings)
    db.add(interaction)
    db.commit()
    db.refresh(interaction)
    return interaction


def get_interactions(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Interaction).offset(skip).limit(limit).all()


def get_interaction(db: Session, interaction_id: UUID):
    interaction = db.query(Interaction).filter(
        Interaction.id == interaction_id).first()
    if not interaction:
        return None
    return


def get_messages(db: Session, interaction_id: UUID):
    interaction = db.query(Interaction).filter(
        Interaction.id == interaction_id).first()
    if not interaction:
        return None
    return interaction.messages


def create_message(db: Session, message: MessageCreate, interaction_id: UUID):
    message = Message(
        interaction_id=interaction_id,
        role="human",
        content=message.content
    )
    db.add(message)
    db.commit()
    db.refresh(message)

    interaction = get_interaction(db, interaction_id)
    if not interaction:
        return None

    # Create initial message from interaction settings
    messages = [{'role': interaction.settings['role'],
                 'content': interaction.settings['prompt']}]

    # Create the list of previous messages
    for message in interaction.messages:
        messages.append({'role': message.role, 'content': message.content})

    # Generate response by AI
    response = g4f.ChatCompletion.create(
        model=interaction.settings['model_name'],
        messages=messages,
    )

    message = Message(
        interaction_id=interaction_id,
        role="ai",
        content=response
    )
    db.add(message)
    db.commit()
    db.refresh(message)

    return message
