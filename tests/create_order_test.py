from helpers import User


class TestCreateOrder:

    def test_create_order_for_user(self, unauthorized_user):

        assert self.__create_order(unauthorized_user)

    def test_create_order_for_authorized_user(self, authorized_user):

        assert self.__create_order(authorized_user)

    def test_create_order_with_ingredients(self, authorized_user):

        ingredients = User.get_ingredients(authorized_user['response_json']['accessToken'])
        response = User.create_order(authorized_user['response_json']['accessToken'], ingredients[0:4])

        ingredients_response = []
        for ingredient in response['response_json']['order']['ingredients']:
            ingredients_response.append(ingredient['_id'])

        assert response["status_code"] == 200 and ingredients[0:4] == ingredients_response

    def test_create_order_without_ingredients(self, authorized_user):
        response = User.create_order(authorized_user['response_json']['accessToken'], [''])

        expected_json = {
            "success": False,
            "message": 'Ingredient ids must be provided'
        }
        assert response["status_code"] == 400 and response["response_json"] == expected_json

    def test_create_order_with_incorrect_ingredient(self, authorized_user):
        response = User.create_order(authorized_user['response_json']['accessToken'], ['hghb'])

        assert response["status_code"] == 500

    @staticmethod
    def __create_order(user):
        ingredients = User.get_ingredients(user['response_json']['accessToken'])
        response = User.create_order(user['response_json']['accessToken'], ingredients[0:4])

        return (response["status_code"] == 200 and response['response_json']["success"] == True and '_id' in
                response['response_json']['order'])

