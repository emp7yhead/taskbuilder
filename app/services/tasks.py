import logging

from fastapi import Depends, HTTPException

from app.settings import settings
from app.utils.reader import build_path, get_data


def get_tasks_tree() -> dict:
    tasks_path = build_path(settings.tasks_file)
    tasks_data = get_data(tasks_path)
    if not tasks_data:
        logging.info('Tasks file empty')
        raise HTTPException(500, 'Tasks are empty')
    return tasks_data['tasks']


def build_tasks_graph(tasks_tree=Depends(get_tasks_tree)):
    return {
        task['name']: task['dependencies']
        for task
        in tasks_tree
    }
