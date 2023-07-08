from fastapi import HTTPException
import pytest
from app.utils.parser import parse
from tests.conftest import get_fixture_path


def test_parse():
    file_data = open(get_fixture_path('expected.json'))
    with pytest.raises(HTTPException):
        parse(file_data, 'json')
