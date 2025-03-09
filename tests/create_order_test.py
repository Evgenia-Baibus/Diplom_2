import allure
import pytest
from data import ExpectedResponses
from helpers import User


class TestCreateOrder:

    @allure.title('Проверка создания заказа без авторизации юзера')
    @allure.description('Отправляем запрос и проверяем, что создается заказ для неавторизованного пользователя')
    def test_create_order_for_user(self, unauthorized_user):
        assert self.__create_order(unauthorized_user)

    @allure.title('Проверка создания заказа с авторизацией юзера')
    @allure.description('Отправляем запрос и проверяем, что создается заказ для авторизованного пользователя')
    def test_create_order_for_authorized_user(self, authorized_user):
        assert self.__create_order(authorized_user)

    @allure.title('Проверка создания заказа с ингредиентами')
    @allure.description('Отправляем запрос и проверяем, что создается заказ с ингредиентами')
    @pytest.mark.parametrize('ingredients_count', [1, 4, None])
    def test_create_order_with_ingredients(self, authorized_user, ingredients_count):
        ingredients = User.get_ingredients(authorized_user['response_json']['accessToken'])
        if ingredients_count:
            ingredients = ingredients[:ingredients_count]
        response = User.create_order(authorized_user['response_json']['accessToken'], ingredients)

        ingredients_response = []
        for ingredient in response['response_json']['order']['ingredients']:
            ingredients_response.append(ingredient['_id'])

        assert response["status_code"] == 200 and ingredients == ingredients_response

    @allure.title('Проверка создания заказа без ингредиентов')
    @allure.description('Отправляем запрос и проверяем, что возвращается ошибка')
    def test_create_order_without_ingredients(self, authorized_user):
        response = User.create_order(authorized_user['response_json']['accessToken'], [''])

        assert response["status_code"] == 400 and response["response_json"] == ExpectedResponses.ingredient_must_be_provided

    @allure.title('Проверка создания заказа с неверным хешем ингредиентов')
    @allure.description('Отправляем запрос и проверяем, что возвращается ошибка')
    def test_create_order_with_incorrect_ingredient(self, authorized_user):
        response = User.create_order(authorized_user['response_json']['accessToken'], ['hghb'])

        assert response["status_code"] == 500

    @staticmethod
    def __create_order(user):
        ingredients = User.get_ingredients(user['response_json']['accessToken'])
        response = User.create_order(user['response_json']['accessToken'], ingredients)

        return (response["status_code"] == 200 and response['response_json']["success"] == True and '_id' in
                response['response_json']['order'])
