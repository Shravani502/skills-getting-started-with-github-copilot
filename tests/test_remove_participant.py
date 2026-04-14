def test_remove_existing_participant(client):
    response = client.delete("/activities/Chess%20Club/participants?email=michael@mergington.edu")

    assert response.status_code == 200
    assert response.json()["message"] == "Removed michael@mergington.edu from Chess Club"

    activity = client.get("/activities").json()["Chess Club"]
    assert "michael@mergington.edu" not in activity["participants"]


def test_remove_nonexistent_activity(client):
    response = client.delete("/activities/Unknown%20Club/participants?email=test@mergington.edu")

    assert response.status_code == 404
    assert response.json()["detail"] == "Activity not found"


def test_remove_nonexistent_participant(client):
    response = client.delete("/activities/Chess%20Club/participants?email=unknown@mergington.edu")

    assert response.status_code == 404
    assert response.json()["detail"] == "Participant not found for this activity"
