from helpers import UserData


class UpdateUserData:

    update_user_arguments = [
            {"email": UserData.updated_email},
            {"password": UserData.updated_password},
            {"name": UserData.updated_name},
            {"name": UserData.updated_name, "password": UserData.updated_password}
        ]