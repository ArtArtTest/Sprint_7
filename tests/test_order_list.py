import requests
from conftest import MAIN_URL
import allure

class TestOrdersList:
    
    @allure.title("Список заказа возвращает тело 'orders'")
    def test_get_order_list_returns_orders(self):
        response = requests.get(f"{MAIN_URL}/orders")

        assert response.status_code == 200
        data = response.json()
        assert "orders" in data
        assert isinstance(data["orders"], list)

