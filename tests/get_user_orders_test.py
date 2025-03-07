import allure
from helpers import UserData, User


class TestGetUserOrders:

    @allure.title('Проверка получения списка заказов для неавторизованного пользователя')
    @allure.description('Отправляем запрос и проверяем, что приходит ответ со списком заказов')
    def test_get_unauthorized_users_orders(self, unauthorized_user):

        assert self.__get_users_orders(unauthorized_user)

    @allure.title('Проверка получения списка заказов для авторизованного пользователя')
    @allure.description('Отправляем запрос и проверяем, что приходит ответ со списком заказов')
    def test_get_authorized_users_orders(self, authorized_user):

        assert self.__get_users_orders(authorized_user)

    @staticmethod
    def __get_users_orders(user):
        response = User.get_orders_for_user(user['response_json']['accessToken'])

        return response["status_code"] == 200 and user["response_json"]["success"] == True