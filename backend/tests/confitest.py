import pytest

from fastapi.testclient import TestClient
from fastapi.encoders import jsonable_encoder

from schemas.user_schema import UserCreate

from main import app
from database.config import init_db
from routes.user_route import router as user_route


def pytest_sessionstart(session):
    """
    Called after the Session object has been created and
    before performing collection and entering the run test loop.
    """
    init_db()


@pytest.fixture
def client():
    app.include_router(user_route)
    return TestClient(app=app)


@pytest.fixture
def test_user():
    return jsonable_encoder(
        UserCreate(
            email="joaopedro2080@hotmail.com",
            first_name="first_name",
            last_name="last_name",
            telefone="telefone",
            address="address",
            id=1,
        )
    )


@pytest.fixture
def user_id():
    return 1

