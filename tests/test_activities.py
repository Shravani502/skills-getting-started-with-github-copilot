def test_get_root_redirects(client):
    response = client.get("/", follow_redirects=False)

    assert response.status_code == 307
    assert response.headers["location"] == "/static/index.html"


def test_get_activities_returns_all(client):
    response = client.get("/activities")

    assert response.status_code == 200
    data = response.json()

    assert isinstance(data, dict)
    assert "Chess Club" in data
    assert "Programming Class" in data
    assert "Gym Class" in data


def test_get_activities_structure(client):
    response = client.get("/activities")
    assert response.status_code == 200

    activity = response.json()["Chess Club"]
    assert activity["description"].startswith("Learn strategies")
    assert activity["schedule"] == "Fridays, 3:30 PM - 5:00 PM"
    assert activity["max_participants"] == 12
    assert isinstance(activity["participants"], list)
