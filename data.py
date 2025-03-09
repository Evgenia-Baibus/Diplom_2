from helpers import User, UserData


class UpdateUserData:

    update_user_arguments = [
        {"email": UserData.updated_email},
        {"password": UserData.updated_password},
        {"name": UserData.updated_name},
        {"name": UserData.updated_name, "password": UserData.updated_password}
    ]


class ExpectedResponses:

    unauthorized = {
        "success": False,
        "message": "You should be authorised"
    }

    @staticmethod
    def success_update(email, name):
        return {
            "success": True,
            "user": {
                "email": email,
                "name": name
            }
        }

    user_already_exist = {
        "success": False,
        "message": "User already exists"
    }

    required_fields_are_not_filled_in = {
        "success": False,
        "message": "Email, password and name are required fields"
    }

    required_fields_are_incorrect = {
        "success": False,
        "message": "email or password are incorrect"

    }

    ingredient_must_be_provided = {
        "success": False,
        "message": 'Ingredient ids must be provided'
    }
