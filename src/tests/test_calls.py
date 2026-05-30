def test_get_calls(client):
    response = client.get("/calls")
    assert response.status_code == 200
    assert len(response.json()["calls"]) > 0



def test_get_call_by_id(client):
    call_id = "1"
    response = client.get(f"/calls/{call_id}")
    assert response.status_code == 200
    assert response.json()["id"] == call_id



def test_get_non_existent_call_by_id(client):
    call_id = "999"
    response = client.get(f"/calls/{call_id}")
    assert response.status_code == 404
    assert response.json()["detail"] == "Call not found"



def test_archive_call(client):
    call_id  = "1"
    response = client.patch(f"/calls/{call_id}/archive")
    assert response.status_code == 200
    assert response.json()["is_archived"] is True



def test_archive_non_existent_call(client):
    call_id = "999"
    response = client.patch(f"/calls/{call_id}/archive")
    assert response.status_code == 404
    assert response.json()["detail"] == "Call not found"



