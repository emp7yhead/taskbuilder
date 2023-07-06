from pathlib import Path

from app.utils.parser import parse
from app.settings import settings


def build_path(file_path: str) -> Path:
    try:
        return Path(settings.builds_dir).resolve() / file_path
    except FileNotFoundError:
        raise FileNotFoundError(
            f'File {file_path} not found in {settings.builds_dir}'
        )


def get_format(file_path: Path) -> str:
    extension = Path(file_path).suffix
    return extension.lower()[1:]


def get_data(file_path: Path) -> dict:
    return parse(open(file_path), get_format(file_path))


def get_tree() -> dict:
    builds_path = build_path(settings.builds_file)
    tasks_path = build_path(settings.tasks_file)
    builds_data = get_data(builds_path)
    tasks_data = get_data(tasks_path)
    return {'build': builds_data, 'tasks': tasks_data}
