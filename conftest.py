import pytest
#from project import create_app
from flask import Flask
from app import app

'''
@pytest.fixture(scope='module')
def test_user():
    flask_app = create_app()
    flask_app.config.from_object('config.TestingConfig')

    with flask_app.test_client() as testing_user:
        with flask_app.app_context():
            yield testing_user
'''
@pytest.fixture(scope='module')
def client():
    app.config['TESTING'] = True
    with app.app_context():
        client = app.test_client()
        yield client