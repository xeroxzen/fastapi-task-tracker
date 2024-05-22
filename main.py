from fastapi import FastAPI
from app.routers import router as task_router
from app.database import Base, engine

app = FastAPI()
Base.metadata.create_all(bind=engine)

app.include_router(task_router, prefix="/api/v1")