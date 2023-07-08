from http import HTTPStatus

from fastapi import APIRouter, Depends

from app.api.v1.build import build_router
from app.api.v1.task import task_router
from app.services.builds import get_builds_tree
from app.services.tasks import get_tasks_tree

main_router = APIRouter()

main_router.include_router(
    task_router,
    prefix='/tasks',
    tags=['tasks'],
)
main_router.include_router(
    build_router,
    prefix='/builds',
    tags=['builds'],
)


@main_router.get(
    '/healthcheck',
    response_model=str,
    status_code=HTTPStatus.OK,
    description='Check existence of needed files for service.',)
async def check_service(
    builds: dict = Depends(get_builds_tree),
    tasks: dict = Depends(get_tasks_tree),
):
    return 'All services available'
