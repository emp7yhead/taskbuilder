def test_get_build_tasks(test_client):
    response = test_client.get(
        '/builds/make_run',
    )
    assert response.status_code == 200
    assert response.json() == ['make_prepare']

    response = test_client.get(
        '/builds/make_test_server',
    )
    assert response.status_code == 200
    assert response.json() == ['make_test', 'make_check']

    response = test_client.get(
        '/builds/call_friends',
    )
    assert response.status_code == 404


def test_get_builds(test_client):
    response = test_client.get(
        '/builds/',
    )
    assert response.status_code == 200
    assert response.json() == ['make_test_server', 'make_run']
