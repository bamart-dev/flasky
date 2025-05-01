

def test_get_all_cats_returns_empty_list_when_db_is_empty(client):
    response = client.get("/cats")
    response_body = response.get_json()

    assert response.status_code == 200
    assert response_body == []


def test_get_one_cat(client, two_saved_cats):
    response = client.get("/cats/1")
    response_body = response.get_json()

    assert response.status_code == 200
    assert response_body == {
        "id": 1,
        "name": "Aang",
        "color": "orange",
        "personality": "orange",
    }
