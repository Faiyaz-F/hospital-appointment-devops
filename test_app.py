from app import app


def test_health():
    client = app.test_client()

    response = client.get("/health")

    assert response.status_code == 200
    assert response.data == b"OK"


def test_get_items():
    client = app.test_client()

    response = client.get("/items")

    assert response.status_code == 200
    assert response.is_json

def test_home_page():
    client = app.test_client()

    response = client.get("/")

    assert response.status_code == 200
    assert b"Hospital Appointment Booking" in response.data
