import pytest

def test_root_redirect(client):
    # Arrange
    # (No setup needed)

    # Act
    response = client.get("/")

    # Assert
    assert response.status_code == 200 or response.status_code == 307  # Redirect or OK
    assert "text/html" in response.headers["content-type"]


def test_get_activities(client):
    # Arrange
    # (No setup needed)

    # Act
    response = client.get("/activities")

    # Assert
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, dict)
    assert "Chess Club" in data
    assert "participants" in data["Chess Club"]
