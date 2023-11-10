from fastapi import FastAPI

from app.models import Base
from app.routers import router
from app.database import engine

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(router)
