from fastapi import FastAPI

from app.settings import settings

app = FastAPI(
    title=settings.app_name,
    description=settings.description,
    version=settings.version,
    contact=settings.contact,
    openapi_tags=settings.tags_metadata,
)


@app.get('/ping')
async def ping():
    return 'pong'
