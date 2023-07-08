import json
from tests.conftest import get_fixture_data


def test_get_tasks(test_client):
    response = test_client.post(
        '/tasks/',
        json={
            'build': 'make_test_server'
        }
    )
    expected = json.loads(get_fixture_data('expected.json'))
    assert response.status_code == 200
    assert response.json() == expected

    response = test_client.post(
        '/tasks/',
        json={
            'build': 'make_run'
        }
    )
    assert response.status_code == 200
    assert response.json() == ['make_prepare']

    response = test_client.post(
        '/tasks/',
        json={
            'build': 'make_wow'
        }
    )
    assert response.status_code == 404
