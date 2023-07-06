from io import TextIOWrapper
import yaml


def parse(data: TextIOWrapper, format_name: str) -> dict:
    if format_name in {'yml', 'yaml'}:
        return yaml.safe_load(data)

    raise ValueError(f'Unknown format: {format_name}')
