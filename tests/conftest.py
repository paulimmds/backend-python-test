import pytest
from alayatodo import app as appl

@pytest.fixture()
def app():
    app = appl
    app.config.update({
        'TESTING': True,
    })

    yield app

@pytest.fixture()
def test_client(app):
    return app.test_client()