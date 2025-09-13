from fastapi.testclient import TestClient

from ai_project.main import app

clint = TestClient(app)


def test_predict_default_multiplier():
    response = clint.post("/predict", json={"x": 3})
    assert response.status_code == 200
    assert response.json() == {"pred": 6}


def test_predict_custom_multiplier():
    response = clint.post("/predict", json={"x": 4, "multiplier": 3})
    assert response.status_code == 200
    assert response.json() == {"pred": 12}


def test_predict_validation_error_for_multiplier_type():
    response = clint.post("/predict", json={"x": 5, "muiltiplier": "invalid"})
    assert response.status_code == 422
