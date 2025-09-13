from fastapi.testclient import TestClient

from ai_project.main import app

client = TestClient(app)


def test_predict_double():
    response = client.post("/predict", json={"x": 5})
    assert response.status_code == 200
    assert response.json() == {"pred": 10}
