import pytest
from app import create_app
from flask import json


@pytest.fixture
def app():

    app = create_app({
        'TESTING': True,
    })

    yield app


@pytest.fixture
def client(app):
    return app.test_client()
