import pytest

# Arrange-Act-Assert pattern for unregister endpoint

def test_unregister_success(client):
    # Arrange
    activity = "Chess Club"
    email = "daniel@mergington.edu"
    url = f"/activities/{activity}/unregister?email={email}"

    # Act
    response = client.post(url)

    # Assert
    assert response.status_code == 200
    assert f"Removed {email} from {activity}" in response.json()["message"]


def test_unregister_not_registered(client):
    # Arrange
    activity = "Chess Club"
    email = "notregistered@mergington.edu"
    url = f"/activities/{activity}/unregister?email={email}"

    # Act
    response = client.post(url)

    # Assert
    assert response.status_code == 400
    assert "not registered" in response.json()["detail"]


def test_unregister_activity_not_found(client):
    # Arrange
    activity = "Nonexistent Club"
    email = "someone@mergington.edu"
    url = f"/activities/{activity}/unregister?email={email}"

    # Act
    response = client.post(url)

    # Assert
    assert response.status_code == 404
    assert "Activity not found" in response.json()["detail"]
