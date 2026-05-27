def test_get_calls(client):
    response = client.get("/calls")
    assert response.status_code == 200
    assert len(response.json()["calls"]) > 0


def test_archive_call(client):
    Id = "1"
    response = client.patch(f"/calls/{Id}/archive")

    assert response.status_code == 200
    assert response.json()["is_archived"] is True

def test_archive_non_existent_call(client):
    response = client.patch("/calls/999/archive")

    assert response.status_code == 404
    assert response.json()["detail"] == "Call not found"



