def test_tasks(test_client):
    response = test_client.post(
        '/tasks',
        json={
            'build': 'make_tests'
        }
    )
    assert response.status_code == 200
    assert response.json() == ['wow']
