from app.utils.reader import build_path, get_data
from app.settings import settings


def get_tasks_tree() -> dict:
    tasks_path = build_path(settings.tasks_file)
    tasks_data = get_data(tasks_path)
    return tasks_data['tasks']


def build_tasks_graph(tasks_tree):
    print(tasks_tree)
    return {
        task['name']: task['dependencies']
        for task
        in tasks_tree
    }


def get_unique(tasks: list[str]) -> list[str]:
    seen = set()
    return [
        task
        for task in tasks
        if task not in seen and not seen.add(task)
    ]
