from fastapi.testclient import TestClient

from ai_project.main import app

client = TestClient(app)


def test_predict_default_multiplier_is_2():
    r = client.post("/predict", json={"x": 5})
    assert r.status_code == 200
    assert r.json() == {"pred": 10}


def test_predict_rejects_wrong_type_for_multiplier():
    r = client.post("/predict", json={"x": 5, "multiplier": "bad"})
    assert r.status_code == 422


def test_predict_rejects_extra_field_when_forbid():
    # 模型已設定 model_config = {"extra": "forbid"}
    r = client.post("/predict", json={"x": 5, "boom": 1})
    assert r.status_code == 422


def test_predict_missing_required_field_x():
    r = client.post("/predict", json={"multiplier": 3})
    assert r.status_code == 422
