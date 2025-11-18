from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_health_endpoint():
    resp = client.get("/health")
    assert resp.status_code == 200
    assert resp.json() == {"status": "ok"}

def test_predict_endpoint():
    resp = client.post("/predict", json={"text": "Good product"})
    assert resp.status_code == 200
    assert resp.json()["sentiment"] == "positive"