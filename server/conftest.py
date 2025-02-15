""" This file is used to define fixtures that can be used in the tests. """
import pytest
from app import app as flask_app


@pytest.fixture
def app():
    """ Create a Flask app for testing. """
    yield flask_app


@pytest.fixture
def client(app):
    """ Create a test client for the Flask app. """
    return app.test_client()
