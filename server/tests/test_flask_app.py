""" Tests for the Flask app. """


def test_generate_story(client):
    """ Test the /generate endpoint. """
    response = client.post(
        "/generate",
        json={"prompt": "Once upon a time..."}
    )
    assert response.status_code == 200
    assert "story" in response.json


def test_update_story(client):
    """ Test the /update endpoint. """
    response = client.post(
        "/update",
        json={"input": "Gandalf fought a dragon."}
    )
    assert response.status_code == 200
    assert "story" in response.json


def test_visualize_story(client):
    """ Test the /visualize endpoint. """
    response = client.get("/visualize")
    assert response.status_code == 200
    assert "nodes" in response.json
    assert "edges" in response.json
