import logging

from fastapi import FastAPI

from app.api.base import main_router
from app.settings import settings

logging.basicConfig(level=logging.INFO)


app = FastAPI(
    title=settings.app_name,
    description=settings.description,
    version=settings.version,
    contact=settings.contact,
    openapi_tags=settings.tags_metadata,
)

app.include_router(main_router)
