import pytest
from data import UpdateUserData, ExpectedResponses
from helpers import User, UserData
from tests.conftest import unauthorized_user


class TestUpdatingUserData:

    @pytest.mark.parametrize('update_data', UpdateUserData.update_user_arguments)
    def test_update_unauthorized_user_data_success(self, unauthorized_user, update_data):
       assert self.__update_user_data(unauthorized_user, update_data )

    @pytest.mark.parametrize('update_data', UpdateUserData.update_user_arguments)
    def test_update_authorized_user_data_success(self, authorized_user, update_data):
        assert self.__update_user_data(authorized_user, update_data)

    def test_update_authorized_user_data_without_token(self, authorized_user):

        user_data = authorized_user["data"]
        user_data["email"] = UserData.updated_email

        response = User.update_user_data(
            '',
            user_data["email"],
            user_data["password"],
            user_data["name"]
        )

        assert response["status_code"] == 401
        assert response["response_json"] == ExpectedResponses.unauthorized

    @staticmethod
    def __update_user_data(user, update_data):
        user_data = user["data"]
        user_data.update(update_data)
        email = user_data["email"]
        name = user_data["name"]


        response = User.update_user_data(
            user['response_json']['accessToken'],
            email,
            user_data["password"],
            name
        )

        return response["status_code"] == 200 and response["response_json"] == ExpectedResponses.success_update(email, name)
