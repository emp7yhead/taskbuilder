import logging

from fastapi import Depends, HTTPException

from app.settings import settings
from app.utils.reader import build_path, get_data


def get_builds_tree() -> dict:
    builds_path = build_path(settings.builds_file)
    builds_data = get_data(builds_path)
    if not builds_data:
        raise HTTPException(500, 'Builds are empty')
    return builds_data['builds']


def get_current_tasks(
    build_name: str,
    builds_tree: dict = Depends(get_builds_tree),
) -> list[str]:
    for build in builds_tree:
        if build['name'] == build_name:
            return build['tasks']
    logging.info(f'Can\'t find "{build_name}" build')
    raise HTTPException(404, 'Build name not found')


def get_all_builds(
    builds_tree: dict = Depends(get_builds_tree),
) -> list[str]:
    return [build['name'] for build in builds_tree]
