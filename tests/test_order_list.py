import requests
from helpers import MAIN_URL
import allure

class TestOrdersList:
    
    @allure.title("Список заказа возвращает тело 'orders'")
    def test_get_order_list_returns_orders(self):
        response = requests.get(f"{MAIN_URL}/orders")
        assert response.status_code == 200
        data = response.json()
        assert "orders" in data
        assert isinstance(data["orders"], list)

#Здравствуйте, тут не очень понятно стало, я же в этом тесте отправляю GET запрос и не создаю данные 
#(поэтому с первого раза не исправил). Спросил у наставника, он сказал, чтобы я Вам написал, чтобы уточнить данный момент
#(еще в гитхабе оставил комментарий)

