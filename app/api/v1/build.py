from http import HTTPStatus
from typing import Annotated

from fastapi import APIRouter, Depends, Path

from app.services.builds import get_all_builds, get_current_tasks

build_router = APIRouter()


@build_router.get(
    '/',
    response_model=list[str],
    status_code=HTTPStatus.OK,
    description='Get available builds.',
)
async def get_builds(
    available_builds=Depends(get_all_builds),
):
    return available_builds


@build_router.get(
    '/{build_name}',
    response_model=list[str],
    status_code=HTTPStatus.OK,
    description='Get build tasks.',
)
async def get_build_tasks(
    build_name: Annotated[
        str,
        Path(..., description="Build name to get tasks list")
    ],
    build_tasks=Depends(get_current_tasks),
):
    return build_tasks
