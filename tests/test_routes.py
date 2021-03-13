def test_healthcheck(client):
    expected_response = {'status': 'up'}
    response = client.get('/healthcheck')
    assert response.status_code == 200
    assert response.json == expected_response



