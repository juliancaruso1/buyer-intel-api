import pytest
from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_list_buyers_returns_five_profiles() -> None:
    response = client.get("/buyers")
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 5
    for item in data:
        assert set(item.keys()) == {
            "id",
            "name",
            "company",
            "industry",
            "revenue_range",
            "location",
        }


def test_get_buyer_by_id() -> None:
    response = client.get("/buyers/1")
    assert response.status_code == 200
    body = response.json()
    assert body["id"] == 1
    assert body["name"] == "Alex Rivera"
    assert body["company"] == "Northwind Logistics"


@pytest.mark.parametrize("buyer_id", [1, 2, 3, 4, 5])
def test_get_buyer_each_valid_id(buyer_id: int) -> None:
    response = client.get(f"/buyers/{buyer_id}")
    assert response.status_code == 200
    assert response.json()["id"] == buyer_id


def test_get_buyer_not_found() -> None:
    response = client.get("/buyers/999")
    assert response.status_code == 404
    assert response.json()["detail"] == "Buyer not found"
