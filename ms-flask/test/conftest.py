import os
import pytest
from app.builder import ApiBuilder
#from app.database import db as _db
from app.config import ConfigTest


TEST_DATABASE_URI = ConfigTest.SQLALCHEMY_DATABASE_URI
app_handler = ApiBuilder(ConfigTest)
app = app_handler.crear_app()


@pytest.fixture(scope='session')
def client(request):
    """Session-wide test `Flask` application."""
    # Establish an application context before running the tests.
    ctx = app.app_context()
    ctx.push()

    def teardown():
        ctx.pop()

    request.addfinalizer(teardown)
    return app.test_client()

'''
@pytest.fixture(scope='session')
def db(client, request):
    """Session-wide test database."""

    def teardown():
        _db.session.rollback()
        _db.drop_all()

    _db.app = client
    _db.create_all()
    app_handler.poblar_db()

    request.addfinalizer(teardown)
    return _db


@pytest.fixture(scope='function')
def session(db, request, mocker):
    """Creates a new database session for a test."""
    connection = db.engine.connect()
    transaction = connection.begin()
    options = dict(bind=connection, binds={})
    session = db.create_scoped_session(options=options)

    db.session = session

    def teardown():
        transaction.rollback()
        connection.close()
        session.remove()

    request.addfinalizer(teardown)
    return session


@pytest.fixture
def token():
    return Usuario('x', 'x', 'x', 'x1', True, None, 'x1').\
        generar_token(1, {'read': '1'})


@pytest.fixture
def token_normal():
    return Usuario('x', 'x', 'x', 'x2', False, None, 'x2').\
        generar_token(2, {'read': '1'})
'''