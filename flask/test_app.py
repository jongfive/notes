import json

def test_get_cars_returns_200(client):
    response = client.get("/api/v1/cars")
    assert response.status_code == 200

def test_get_cars_returns_list(client):
    response = client.get("/api/v1/cars")
    data = json.loads(response.data.decode("utf-8"))
    assert isinstance(data, list)

def test_get_car_returns_200(client):
    response = client.get("/api/v1/cars/1")
    assert response.status_code == 200

def test_get_car_returns_dict(client):
    response = client.get("/api/v1/cars/1")
    data = json.loads(response.data.decode("utf-8"))
    assert isinstance(data, dict)