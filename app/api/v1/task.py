from http import HTTPStatus
from fastapi import APIRouter, Depends

from app.schemas.build import BuildIn

task_router = APIRouter()


@task_router.post(
    '/',
    response_model=list[str],
    status_code=HTTPStatus.OK,
    description='Get tasks for specified build.',
)
async def get_tasks(
    build_name: BuildIn,
):
    return ['wow']
