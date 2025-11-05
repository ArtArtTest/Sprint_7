import requests
import random
import string

MAIN_URL = "https://qa-scooter.praktikum-services.ru/api/v1"


def generate_random_string(length=10):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(length))
        return random_string

def register_new_courier_and_return_login_password():
    login_pass = []

    login = generate_random_string(10)
    password = generate_random_string(10)
    first_name = generate_random_string(10)

    payload = {
        "login": login,
        "password": password,
        "firstName": first_name
    }

    response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier', data=payload)

    if response.status_code == 201:
        login_pass.append(login)
        login_pass.append(password)
        login_pass.append(first_name)

    return login_pass


def delete_courier(login, password):
    login_resp = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier/login', data={"login": login, "password": password})
    if login_resp.status_code == 200:
        courier_id = login_resp.json().get("id")
        requests.delete(f'https://qa-scooter.praktikum-services.ru/api/v1/courier/{courier_id}')

def order_paylord(color=None):
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
    return payload

def create_order(color=None):
    payload = order_paylord(color)
    return requests.post(f"{MAIN_URL}/orders", json=payload)

def cancel_order_by_track(track_number):
    url = f"{MAIN_URL}/orders/cancel"
    params = {"track": track_number}
    return requests.put(url, params=params)
