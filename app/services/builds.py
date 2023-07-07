import logging

from fastapi import HTTPException

from app.schemas.build import BuildIn
from app.settings import settings
from app.utils.reader import build_path, get_data


def get_builds_tree():
    builds_path = build_path(settings.builds_file)
    builds_data = get_data(builds_path)
    return builds_data['builds']


def get_current_tasks(builds: dict, build_name: BuildIn) -> list[str]:
    for build in builds:
        if build['name'] == build_name.build:
            return build['tasks']
    logging.info(f'Can\'t find "{build_name.build}" build')
    raise HTTPException(404, 'Build name not found')
