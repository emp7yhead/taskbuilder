from io import TextIOWrapper
import logging

import yaml
from fastapi import HTTPException


def parse(data: TextIOWrapper, format_name: str) -> dict:
    if format_name in {'yml', 'yaml'}:
        return yaml.safe_load(data)
    logging.info('Build files must be yml or yaml')
    raise HTTPException(500, f'Unknown format: {format_name}')
