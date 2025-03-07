import allure
import pytest
from helpers import User, UserData


class TestSignInUser:

    @allure.title('Проверка успешной авторизации юзера')
    @allure.description('Отправляем запрос и проверяем, что юзер может авторизоваться')
    def test_sign_in_user_success(self, authorized_user):

        assert authorized_user["status_code"] == 200 and authorized_user["response_json"]["success"] == True


    @allure.title('Проверка возвращения ошибки, если не указан емейл или пароль')
    @allure.description('Отправляем запрос и проверяем, что если емейла или пароля нет, то запрос возвращает ошибку')
    @pytest.mark.parametrize(
        'email, password',
        [
            [UserData.data_with_incorrect_email["email"], UserData.data_with_incorrect_email["password"]],
            [UserData.data_with_incorrect_password["email"], UserData.data_with_incorrect_password["password"]]
        ]
    )
    @allure.title('Проверка возвращения ошибки, если указан неправильный емейл или пароль')
    @allure.description('Отправляем запрос и проверяем, что если неправильно указать логин или пароль, то система вернёт ошибку')
    def test_sign_in_user_with_incorrect_email_or_password(self, email, password):

        response = User.sign_in_user_and_get_user_data(email, password)

        expected_json = {
            "success": False,
            "message": "email or password are incorrect"
        }

        assert response["status_code"] == 401 and response["response_json"] == expected_json
