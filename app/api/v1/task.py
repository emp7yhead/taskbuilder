from http import HTTPStatus

from fastapi import APIRouter, Depends

from app.schemas.build import BuildIn
from app.services.builds import get_builds_tree, get_current_tasks
from app.services.tasks import build_tasks_graph
from app.utils.tree import get_dependencies

task_router = APIRouter()


@task_router.post(
    '/',
    response_model=list[str],
    status_code=HTTPStatus.OK,
    description='Get tasks for specified build.',
)
async def get_tasks(
    build_name: BuildIn,
    builds_tree=Depends(get_builds_tree),
    tasks_graph=Depends(build_tasks_graph),
):
    current_tasks: list[str] = get_current_tasks(
        build_name.build, builds_tree
    )
    return get_dependencies(tasks_graph, current_tasks)
