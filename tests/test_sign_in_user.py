import allure
import pytest

from data import ExpectedResponses
from helpers import User, UserData


class TestSignInUser:

    @allure.title('Проверка успешной авторизации юзера')
    @allure.description('Отправляем запрос и проверяем, что юзер может авторизоваться')
    def test_sign_in_user_success(self, authorized_user):
        assert authorized_user["status_code"] == 200
        assert authorized_user["response_json"]["success"] == True


    @allure.title('Проверка возвращения ошибки, если не указан емейл или пароль')
    @allure.description('Отправляем запрос и проверяем, что если емейла или пароля нет, то запрос возвращает ошибку')
    @pytest.mark.parametrize(
        'email, password',
        [
            [UserData.data_with_incorrect_email["email"], UserData.data_with_incorrect_email["password"]],
            [UserData.data_with_incorrect_password["email"], UserData.data_with_incorrect_password["password"]]
        ]
    )
    def test_sign_in_user_with_incorrect_email_or_password(self, email, password):
        response = User.sign_in_user_and_get_user_data(email, password)

        assert response["status_code"] == 401
        assert response["response_json"] == ExpectedResponses.required_fields_are_incorrect
