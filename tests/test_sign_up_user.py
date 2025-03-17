import allure
import pytest
import requests
from data import ExpectedResponses
from helpers import User, UserData
from urls import Urls


class TestSignUpUser:

    @allure.title('Проверка успешного cоздания юзера')
    @allure.description('Отправляем запрос и проверяем, что юзера можно создать')
    def test_user_sign_up_success(self, unauthorized_user):
        assert unauthorized_user["status_code"] == 200
        assert unauthorized_user["response_json"]["success"] == True

    @allure.title('Проверка возвращения ошибки при регистрации уже существующего пользователя')
    @allure.description('Отправляем запрос и проверяем, что запрос возвращает ошибку')
    def test_user_sign_up_failure_for_already_registered(self, unauthorized_user):
        user_data = User.sign_up_and_get_user_data()

        assert user_data["status_code"] == 403
        assert user_data["response_json"] == ExpectedResponses.user_already_exist

    @allure.title('Проверка возвращения ошибки, если не указаны обязательные поля')
    @allure.description('Отправляем запрос и проверяем, что если обязательные поля не заполнены, то запрос возвращает ошибку')
    @pytest.mark.parametrize('data', [UserData.data_without_email, UserData.data_without_password, UserData.data_without_name])
    def test_user_sign_up_failure_without_required_field(self, data):
        response = requests.post(Urls.SIGN_UP, data=data)

        assert response.status_code == 403
        assert response.json() == ExpectedResponses.required_fields_are_not_filled_in



