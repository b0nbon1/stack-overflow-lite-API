import pytest
from flask import json

class AuthActions(object):
    def __init__(self, client):
        self._client = client

    def login(self, username='test', password='testpytest'):
        return self._client.post(
            '/auth/login',
            data=json.dumps({'username': username, 'password': password}), content_type='application/json'
        )

    def register(self, username='test1', email='test1@test.com', password='testpytest', confirm_password='testpytest'):
        return self._client.post(
            '/auth/register',
            data=json.dumps({'username': username, 'email': email,
                             'password': password, 'confirm_password': confirm_password}),
            content_type='application/json'
        )


@pytest.fixture
def auth(client):
    return AuthActions(client)

def test_login(client, auth):
    response = auth.login()

    assert response.status_code == 200


'email'


@pytest.mark.parametrize(('username', 'password', 'message'), (
    ('not', 'test', b'user not found'),
    ('test', 'guess', b'wrong password'),
    ('test', 'testpytest', b'Successfully Logged In')
))
def test_login_validate_input(auth, username, password, message):
    response = auth.login(username, password)
    assert message in response.data


def test_register(client, auth):
    response = auth.register()
    assert response.status_code == 200


@pytest.mark.parametrize(('username', 'email', 'password', 'confirm_password', 'message'), (
    ('te', 'test1@test.com', 'testpytest', 'testpytest', b'invalid username'),
    ('test', 'test1@test.com', 'testpytest', 'testpytest', b'username exists'),
    ('test2', 'test', 'testpytest', 'testpytest', b'invalid email'),
    ('test3', 'test1@test.com', 'test', 'test', b'invalid password'),
    ('test4', 'test1@test.com', 'testpytest', 'test', b'Passwords don\'t match'),
    ('test5', 'test1@test.com', 'testpytest',
     'testpytest', b'user successfull registered!')
))
def test_register_validate_input(auth, username, email, password, confirm_password, message):
    response = auth.register(username, email, password, confirm_password)

    assert message in response.data
