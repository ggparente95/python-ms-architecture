import pytest

@pytest.fixture
def hardcoded_users():
    users = [
        {"name": "Pablo", "surname": "Rodriguez"},
        {"name": "Juan", "surname": "Perez"},
        {"name": "Martin", "surname": "Rodriguez"}
    ]
    return users