import pytest
from helpers import register_new_courier_and_return_login_password, delete_courier, create_order, cancel_order_by_track

@pytest.fixture
def create_courier():
    login_pass = register_new_courier_and_return_login_password()
    if not login_pass:
        pytest.fail("Курьер не создан")

    login, password, first_name = login_pass
    yield login, password, first_name
    delete_courier(login, password)

def managed_order():
    response = create_order()
    assert response.status_code == 201, "Не удалось создать заказ для теста"
    track = response.json()["track"]
    yield track  
    cancel_response = cancel_order_by_track(track)
    assert cancel_response.status_code == 200