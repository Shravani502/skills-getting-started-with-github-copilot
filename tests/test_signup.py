from src.app import activities


def test_signup_valid_student(client):
    response = client.post("/activities/Chess%20Club/signup?email=test@mergington.edu")

    assert response.status_code == 200
    assert response.json()["message"] == "Signed up test@mergington.edu for Chess Club"

    activity = client.get("/activities").json()["Chess Club"]
    assert "test@mergington.edu" in activity["participants"]


def test_signup_nonexistent_activity(client):
    response = client.post("/activities/Unknown%20Club/signup?email=test@mergington.edu")

    assert response.status_code == 404
    assert response.json()["detail"] == "Activity not found"


def test_signup_duplicate_prevention(client):
    response = client.post("/activities/Chess%20Club/signup?email=michael@mergington.edu")

    assert response.status_code == 400
    assert response.json()["detail"] == "Student already signed up for this activity"


def test_signup_max_participants_limit(client):
    activities["Full Club"] = {
        "description": "A full activity",
        "schedule": "Tomorrow, 4:00 PM",
        "max_participants": 1,
        "participants": ["already@mergington.edu"],
    }

    response = client.post("/activities/Full%20Club/signup?email=newstudent@mergington.edu")

    assert response.status_code == 400
    assert response.json()["detail"] == "Activity is full"
