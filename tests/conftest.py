import pytest
from helpers import User, UserData


@pytest.fixture
def unauthorized_user():
    user_data = User.sign_up_and_get_user_data()
    yield user_data
    User.delete_user(user_data['response_json']['accessToken'])

@pytest.fixture
def authorized_user(unauthorized_user):
    user_data = unauthorized_user['data']
    sign_in_user_data = User.sign_in_user_and_get_user_data(user_data['email'], user_data['password'], user_data["name"])
    return sign_in_user_data



