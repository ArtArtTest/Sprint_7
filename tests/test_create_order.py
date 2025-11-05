import pytest
from helpers import create_order, cancel_order_by_track
import allure

class TestCreateOrder:
    
    @allure.title("Создание заказа с указанием цвета")
    @pytest.mark.parametrize("color", [None, ["BLACK"], ["GREY"], ["BLACK", "GREY"]])
    def test_create_order_with_various_colors(self, color):
        response = create_order(color)
        assert response.status_code == 201
        track = response.json()["track"]
        assert "track" in response.json()
        cancel_resp = cancel_order_by_track(track)
        assert cancel_resp.status_code == 200
        
        


