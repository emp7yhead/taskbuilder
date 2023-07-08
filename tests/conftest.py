from pathlib import Path
from fastapi import HTTPException
import pytest

from fastapi.testclient import TestClient
import yaml

from app.main import app
from app.services.builds import get_builds_tree
from app.services.tasks import get_tasks_tree


def get_fixture_path(file_name):
    current_dir = Path().cwd()
    return current_dir.joinpath(current_dir, 'tests/fixtures', file_name)


def read(file_path):
    with Path.open(file_path) as f:
        result = f.read()
    return result


def get_fixture_data(file_name):
    return read(get_fixture_path(file_name))


def get_fake_builds_tree():
    test_builds = get_fixture_data('test_builds.yml')
    test_builds_data = yaml.safe_load(test_builds)
    return test_builds_data['builds']


def get_fake_tasks_tree():
    test_tasks = get_fixture_data('test_tasks.yml')
    test_tasks_data = yaml.safe_load(test_tasks)
    return test_tasks_data['tasks']


@pytest.fixture(scope='function')
def test_client():
    app.dependency_overrides[get_builds_tree] = get_fake_builds_tree
    app.dependency_overrides[get_tasks_tree] = get_fake_tasks_tree
    client = TestClient(app)
    yield client
