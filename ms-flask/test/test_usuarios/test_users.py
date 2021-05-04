import pytest
from flask import jsonify


def test_get_users(client, hardcoded_users):
    resp = client.get('/users')
    assert resp.status_code == 200
    assert resp.get_json() == hardcoded_users
