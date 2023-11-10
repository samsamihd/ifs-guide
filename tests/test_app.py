from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_get_interactions():
    response = client.get("/interactions/",
                          headers={"X-Token": "coneofsilence"})
    assert response.status_code == 200


def test_create_interaction():
    response = client.post(
        "/interactions/",
        headers={"X-Token": "coneofsilence"},
        json={
            "settings": {
                "model_name": "gpt-3.5-turbo",
                "role": "System",
                "prompt": "As a helpful IFS therapist chatbot, your role is to guide users through a simulated IFS session in a safe and supportive manner with a few changes to the exact steps of the IFS model."
            }
        },
    )
    assert response.status_code == 200
