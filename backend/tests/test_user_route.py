from fastapi import status


def test_create_user_route(client, test_user):
    response = client.post(url="/users", json=test_user)

    print(f"Tnesss {response}")

    assert response.status_code == status.HTTP_201_CREATED

    print(f"JJJSJS {response.json()}")

    created_user = response.json()

    assert created_user["time_created"] == created_user["time_updated"]
    assert test_user["first_name"] == created_user["first_name"]
    assert test_user["last_name"] == created_user["last_name"]
    assert test_user["email"] == created_user["email"]
    assert test_user["telefone"] == created_user["telefone"]
    assert test_user["address"] == created_user["address"]


def test_create_user_conflict(client, test_user):
    response = client.post(url="/users", json=test_user)
    assert response.status_code == status.HTTP_409_CONFLICT

    print(f"JJJSJS {response.json()}")


def test_get_users_ok(client):
    response = client.get("/users")
    assert response.status_code == status.HTTP_200_OK
    assert isinstance(response.json(), list)
    assert len(response.json()) == 1

    print(f"JJJSJS {response.json()}")


def test_get_user_by_id_ok(client, user_id, test_user):
    response = client.get(f"/users/{user_id}")
    assert response.status_code == status.HTTP_200_OK
    assert isinstance(response.json(), dict)

    fetched_user = response.json()
    assert test_user["email"] == fetched_user["email"]


def test_get_user_by_id_not_found(client, user_id):
    response = client.get(f"/users/{user_id-1}")
    assert response.status_code == status.HTTP_404_NOT_FOUND


def test_delete_user_no_content(client, user_id):
    response = client.delete(f"/users/{user_id}")
    assert response.status_code == status.HTTP_204_NO_CONTENT

    new_response = client.get(f"/users/{user_id}")
    assert new_response.status_code == status.HTTP_404_NOT_FOUND
