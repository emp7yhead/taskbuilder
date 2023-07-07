from app.utils.reader import get_format
from tests.conftest import get_fixture_path


def test_get_format():
    test_path = get_fixture_path('builds.yml')
    assert get_format(test_path) == 'yml'

    test_path = get_fixture_path('expected.json')
    assert get_format(test_path) == 'json'
