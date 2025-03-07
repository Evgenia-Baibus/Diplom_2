import pytest
from helpers import User, UserData


class TestSignInUser:

    def test_sign_in_user_success(self, authorized_user):

        assert authorized_user["status_code"] == 200 and authorized_user["response_json"]["success"] == True

    @pytest.mark.parametrize(
        'email, password',
        [
            [UserData.data_with_incorrect_email["email"], UserData.data_with_incorrect_email["password"]],
            [UserData.data_with_incorrect_password["email"], UserData.data_with_incorrect_password["password"]]
        ]
    )
    def test_sign_in_user_with_incorrect_login_or_password(self, email, password):

        response = User.sign_in_user_and_get_user_data(email, password)

        expected_json = {
            "success": False,
            "message": "email or password are incorrect"
        }

        assert response["status_code"] == 401 and response["response_json"] == expected_json
