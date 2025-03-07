import pytest
import requests
from helpers import User, UserData
from urls import Urls


class TestSignUpUser:

    def test_user_sign_up_success(self, unauthorized_user):
        assert unauthorized_user["status_code"] == 200 and unauthorized_user["response_json"]["success"] == True

    def test_user_sign_up_failure_for_already_registered(self, unauthorized_user):
        user_data = User.sign_up_and_get_user_data()

        expected_json = {
            "success": False,
            "message": "User already exists"
         }
        assert user_data["status_code"] == 403 and user_data["response_json"] == expected_json

    @pytest.mark.parametrize('data', [UserData.data_without_email, UserData.data_without_password, UserData.data_without_name])
    def test_user_sign_up_failure_without_required_field(self, data):
        response = requests.post(Urls.SIGN_UP, data=data)
        expected_json = {
            "success": False,
            "message": "Email, password and name are required fields"
        }

        assert response.status_code == 403 and response.json() == expected_json



