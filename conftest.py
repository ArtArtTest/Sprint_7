import pytest
from helpers import register_new_courier_and_return_login_password, delete_courier, order_paylord

@pytest.fixture
def create_courier():
    login_pass = register_new_courier_and_return_login_password()
    if not login_pass:
        pytest.fail("Курьер не создан")

    login, password, first_name = login_pass
    yield login, password, first_name
    delete_courier(login, password)

@pytest.fixture
def create_order_fixture():
    response = order_paylord()
    assert response.status_code == 201, "Не удалось создать заказ"
    track = response.json()["track"]
    yield track
    print(f"Заказ {track} завершён")