from fastapi import APIRouter

from app.api.v1.task import task_router

main_router = APIRouter()

main_router.include_router(
    task_router,
    prefix='/tasks',
    tags=['tasks'],
)


@main_router.get('/ping')
async def ping():
    return 'pong'
