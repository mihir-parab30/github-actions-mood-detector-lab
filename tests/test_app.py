from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_health_endpoint():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_predict_endpoint():
    response = client.post("/predict", json={"text": "Good service"})
    assert response.status_code == 200
    assert response.json()["sentiment"] == "positive"
