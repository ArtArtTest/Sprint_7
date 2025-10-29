import pytest
import requests
from conftest import MAIN_URL
import allure

class TestCreateOrder:
    
    @allure.title("Создание заказа с указанием цвета")
    @pytest.mark.parametrize("color", [None, ["BLACK"], ["GREY"], ["BLACK", "GREY"]])
    def test_create_order_with_various_colors(self, color):
        payload = {
            "firstName": "Saske",
            "lastName": "Uchiha",
            "address": "Moscow",
            "metroStation": 4,
            "phone": "+7 800 355 35 35",
            "rentTime": 5,
            "deliveryDate": "2025-10-30",
            "comment": "Privet Rewiewer"
        }
        if color is not None:
            payload["color"] = color

        response = requests.post(f"{MAIN_URL}/orders", json=payload)

        assert response.status_code == 201
        assert "track" in response.json()


