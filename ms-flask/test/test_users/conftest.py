import pytest
from app.models.Area import Area
from app.models.User import User


@pytest.fixture
def management_fixture(session):
    a = Area(name="Management")
    session.add(a)
    session.commit()

@pytest.fixture
def user_1(session, management_fixture):
    user = {
        "name": "Pablo",
        "surname": "Rodriguez",
        "email": "test@gmail.com",
        "password": "maxpass",
        "admin": True,
        "dni": "2222",
        "area_id": 2
    }
    return user

@pytest.fixture
def modified_user_1(session, user_1):
    u = User(**user_1)
    session.add(u)
    session.commit()
    user = {
        "name": "Pablo Changed",
        "surname": "Rodriguez Two",
        "email": "test@gmail.com",
        "admin": True,
        "dni": "22226",
        "area_id": 2
    }
    return user