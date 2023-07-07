from pathlib import Path

from app.settings import settings
from app.utils.parser import parse


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
