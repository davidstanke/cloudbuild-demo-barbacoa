import app

import pytest


@pytest.fixture
def client():
    app.app.testing = True
    return app.app.test_client()


def test_definition(client):
    r = client.get("/test")
    assert r.status_code == 200

    r = client.get("/error")
    assert r.status_code == 500