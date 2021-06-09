import pytest
from flask import jsonify


def test_get_all_users(client, session):
    resp = client.get('/users')
    users = resp.get_json()
    assert len(users) == 2


def test_create_user(client, session, user_1):
    resp = client.post('/users', json=user_1)
    json_data = resp.get_json()
    assert resp.status_code == 200
    assert json_data['id'] == 3


def test_update_user(client, session, modified_user_1):
    resp = client.put('/users/3', json=modified_user_1)
    assert resp.status_code == 200
    resp = client.get('/users/3')
    user_data = resp.get_json()
    assert user_data['dni'] == modified_user_1['dni']


def test_delete_user(client, session, modified_user_1):
    resp = client.delete('/users/3')
    assert resp.status_code == 200
    resp = client.get('/users/3')
    assert resp.status_code == 404