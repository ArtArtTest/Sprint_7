import pytest
import requests
from helpers import generate_random_string, MAIN_URL
import allure

class TestCreateCourier:
    
    @allure.title("Успешное создание курьера")
    def test_create_courier_success(self):
        login = generate_random_string()
        password = generate_random_string()
        first_name = generate_random_string()
        payload = {"login": login, "password": password, "firstName": first_name}
        response = requests.post(f"{MAIN_URL}/courier", data = payload)
        assert response.status_code == 201
        assert response.json() == {"ok": True}
    
    @allure.title("Нельзя создать курьеров с одинаковым логином")
    def test_create_duplicate_courier_fails(self, create_courier):
        login, _, _ = create_courier
        payload = {"login": login, "password": "1234", "firstName": "saske"}
        response = requests.post(f"{MAIN_URL}/courier", data = payload)
        assert response.status_code == 409
        assert response.json().get("message") =="Этот логин уже используется. Попробуйте другой."
    
    @allure.title("Нельзя создать курьера без обязательного поля")
    @pytest.mark.parametrize("missing_field", ["login", "password"])
    def test_create_courier_missing_required_field_fails(self, missing_field):
        data = {
            "login": generate_random_string(),
            "password": generate_random_string(),
            "firstName": generate_random_string()
        } 
        data.pop(missing_field)
        response = requests.post(f"{MAIN_URL}/courier", data = data)
        assert response.status_code == 400
        assert response.json().get("message") =="Недостаточно данных для создания учетной записи"



