import pytest
import requests
from helpers import MAIN_URL
import allure

class TestLoginCourier:
    
    @allure.title("Успешная авторизация курьера, возвращается id")
    def test_login_success(self, create_courier):
        login, password, _ = create_courier
        response = requests.post(f"{MAIN_URL}/courier/login", data={"login": login, "password": password})
        assert response.status_code == 200
        assert "id" in response.json()
    
    @allure.title("Нельзя авторизоваться без обязательного поля")
    @pytest.mark.parametrize("missing_field", ["login", "password"])
    def test_login_missing_field_fails(self, missing_field):
        data = {"login": "ninja", "password": "1234"}
        data.pop(missing_field)
        response = requests.post(f"{MAIN_URL}/courier/login", data=data)
        assert response.status_code == 400
        assert "Недостаточно данных для входа" in response.text
    #тест с паролем падает, спросил у наставника, передаю его цитату:
    # "Да и пусть падают, что ж поделаешь-то,мы то никак не можем повлиять на то как сервер себя ведет, нам главное автотесты верно написать)"  
    
    @allure.title("Нельзя авторизоваться с неправильным паролем")
    def test_login_with_wrong_password_fails(self, create_courier):
        login, _, _ = create_courier
        response = requests.post(f"{MAIN_URL}/courier/login", data={"login": login, "password": "saskevernis"})
        assert response.status_code == 404
        assert response.json().get("message") =="Учетная запись не найдена"
    
    @allure.title("Нельзя авторизоваться с неправильным логином")
    def test_login_with_wrong_login_fails(self, create_courier):
        _, password, _ = create_courier
        response = requests.post(f"{MAIN_URL}/courier/login", data={"login": "saskevernis", "password": password})
        assert response.status_code == 404
        assert response.json().get("message") =="Учетная запись не найдена"
    
    @allure.title("Ошибка при авторизации несуществующего пользователя")
    def test_login_no_exist_user_fails(self):
        response = requests.post(f"{MAIN_URL}/courier/login", data={"login": "narutogdesaske", "password": "12345"})
        assert response.status_code == 404
        assert response.json().get("message") =="Учетная запись не найдена"
    
    @allure.title("Передача всех обязательных полей для успешной авторизации")
    def test_login_with_all_required_fields_success(self, create_courier):
        login, password, _ = create_courier
        response = requests.post(f"{MAIN_URL}/courier/login", data={"login": login, "password": password})
        assert response.status_code == 200
        assert "id" in response.json()

