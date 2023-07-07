from pathlib import Path
import pytest

from fastapi.testclient import TestClient
import yaml

from app.main import app
from app.utils.reader import get_tree


def get_fixture_path(file_name):
    current_dir = Path().cwd()
    return current_dir.joinpath(current_dir, 'tests/fixtures', file_name)


def read(file_path):
    with Path.open(file_path) as f:
        result = f.read()
    return result


def get_fixture_data(file_name):
    return read(get_fixture_path(file_name))


@pytest.fixture(scope='function')
def test_client():
    app.dependency_overrides[get_tree] = get_fake_tree
    client = TestClient(app)
    yield client


def get_fake_tree():
    test_builds = get_fixture_data('test_builds.yml')
    test_tasks = get_fixture_data('test_tasks.yml')
    test_builds_data = yaml.safe_load(test_builds)
    test_tasks_data = yaml.safe_load(test_tasks)
    return {
        **test_builds_data,
        **test_tasks_data,
    }
