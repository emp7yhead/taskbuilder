import logging
from pathlib import Path

from fastapi import HTTPException

from app.settings import settings
from app.utils.parser import parse


def build_path(file_path: str) -> Path:
    return Path(settings.builds_dir).resolve() / file_path


def get_format(file_path: Path) -> str:
    extension = Path(file_path).suffix
    return extension.lower()[1:]


def get_data(file_path: Path) -> dict:
    try:
        return parse(open(file_path), get_format(file_path))
    except FileNotFoundError:
        logging.info(
            f"File '{file_path.parts[-1]}' not found in /{settings.builds_dir}"
        )
        raise HTTPException(
            500,
            f"Can't get needed files in /{settings.builds_dir}",
        )
