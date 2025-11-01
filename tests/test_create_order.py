import pytest
import requests
from helpers import MAIN_URL, order_paylord
import allure

class TestCreateOrder:
    
    @allure.title("Создание заказа с указанием цвета")
    @pytest.mark.parametrize("color", [None, ["BLACK"], ["GREY"], ["BLACK", "GREY"]])
    def test_create_order_with_various_colors(self, color):
        payload = order_paylord(color) 
        response = requests.post(f"{MAIN_URL}/orders", json=payload)
        assert response.status_code == 201
        assert "track" in response.json()


