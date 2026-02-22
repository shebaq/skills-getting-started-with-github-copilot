import pytest

# Arrange-Act-Assert pattern for signup endpoint

def test_signup_success(client):
    # Arrange
    activity = "Chess Club"
    email = "newstudent@mergington.edu"
    url = f"/activities/{activity}/signup?email={email}"

    # Act
    response = client.post(url)

    # Assert
    assert response.status_code == 200
    assert f"Signed up {email} for {activity}" in response.json()["message"]


def test_signup_duplicate(client):
    # Arrange
    activity = "Chess Club"
    email = "michael@mergington.edu"  # Already signed up
    url = f"/activities/{activity}/signup?email={email}"

    # Act
    response = client.post(url)

    # Assert
    assert response.status_code == 400
    assert "already signed up" in response.json()["detail"]


def test_signup_activity_not_found(client):
    # Arrange
    activity = "Nonexistent Club"
    email = "someone@mergington.edu"
    url = f"/activities/{activity}/signup?email={email}"

    # Act
    response = client.post(url)

    # Assert
    assert response.status_code == 404
    assert "Activity not found" in response.json()["detail"]
