from fastapi.testclient import TestClient

from ai_project.main import app

client = TestClient(app)


def test_health_ok():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_info_has_routes_and_version():
    r = client.get("/info")
    assert r.status_code == 200

    info = r.json()

    # route should be a list of strings
    assert "routes" in info
    assert isinstance(info["routes"], list)

    # top level keys in dict
    assert "version" in info
    # type checks: should be string
    assert isinstance(info["version"], str)
    assert "started_at" in info
    assert isinstance(info["started_at"], str)

    # List should include at least these routes
    assert "/health" in info["routes"]
    assert "/info" in info["routes"]
    assert "/predict" in info["routes"]
