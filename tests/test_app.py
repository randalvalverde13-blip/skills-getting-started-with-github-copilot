from fastapi.testclient import TestClient

from src.app import app

client = TestClient(app)


def test_unregister_participant_removes_email_from_activity():
    response = client.delete("/activities/Chess%20Club/participants/michael%40mergington.edu")

    assert response.status_code == 200
    assert "michael@mergington.edu" not in client.get("/activities").json()["Chess Club"]["participants"]


def test_unregister_missing_activity_returns_404():
    response = client.delete("/activities/Unknown%20Club/participants/test%40example.com")

    assert response.status_code == 404
