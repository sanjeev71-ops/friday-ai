from contextlib import asynccontextmanager

from fastapi import FastAPI

from core.config.settings import settings
from core.logging.logger import logger

from apps.api.routes.v1.chat import router as chat_router
from apps.api.middleware.error_handler import global_exception_handler


@asynccontextmanager
async def lifespan(app: FastAPI):

    logger.info("Starting FRIDAY backend")

    yield

    logger.info("Shutting down FRIDAY backend")


app = FastAPI(title=settings.APP_NAME, lifespan=lifespan)

app.include_router(chat_router, prefix="/api/v1", tags=["chat"])

app.add_exception_handler(Exception, global_exception_handler)


@app.get("/health")
async def health():
    return {"status": "running"}
