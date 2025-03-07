
import requests
from faker import Faker
from urls import Urls

class UserDataGeneration:

    @staticmethod
    def generate_valid_user_data():
        fake = Faker()

        email = fake.email()
        password = fake.password()
        name = fake.name()

        return {
            "email": email,
            "password": password,
            "name": name
        }

    @staticmethod
    def generate_user_data_without_email_field():
        fake = Faker()

        password = fake.password()
        name = fake.name()

        return {
            "email": '',
            "password": password,
            "name": name
        }

    @staticmethod
    def generate_user_data_without_password_field():
        fake = Faker()

        email = fake.email()
        name = fake.name()

        return {
            "email": email,
            "password": "",
            "name": name
        }

    @staticmethod
    def generate_user_data_without_name_field():
        fake = Faker()

        email = fake.email()
        password = fake.password()

        return {
            "email": email,
            "password":  password,
            "name": ''
        }

    @staticmethod
    def generate_updated_user_data():
        fake = Faker()

        email = fake.email()
        password = fake.password()
        name = fake.name()

        return {
            "email": email,
            "password": password,
            "name": name
        }

class UserData:

    data_with_incorrect_email = {
        "email": '111xxg',
        "password": 'password'
    }

    data_with_incorrect_password = {
        "email": 'evgenia_baibus@gmail.com',
        "password": 'password12'
    }

    valid_data = UserDataGeneration.generate_valid_user_data()

    data_without_email= UserDataGeneration.generate_user_data_without_email_field()
    data_without_password = UserDataGeneration.generate_user_data_without_password_field()
    data_without_name = UserDataGeneration.generate_user_data_without_name_field()

    updated_email = UserDataGeneration.generate_updated_user_data()['email']
    updated_password = UserDataGeneration.generate_updated_user_data()['password']
    updated_name = UserDataGeneration.generate_updated_user_data()['name']

class User:

    @staticmethod
    def sign_up_and_get_user_data():
        data = UserData.valid_data
        response = requests.post(Urls.SIGN_UP, data=data)
        return {"data": data, "response_json": response.json(), "status_code": response.status_code}

    @staticmethod
    def delete_user(access_token):
        headers = {"Authorization": access_token}
        response = requests.delete(Urls.DELETE_USER,  headers= headers)
        return response

    @staticmethod
    def sign_in_user_and_get_user_data(email, password, name = None):
        data = {
            "email": email,
            "password": password,
        }
        if name:
            data["name"] = name

        response = requests.post(Urls.SIGN_IN, data=data)
        return {"data":data, "response_json": response.json(), "status_code": response.status_code}

    @staticmethod
    def update_user_data(access_token, email, password, name):
        headers = {"Authorization": access_token}
        updated_data = {
            "email": email,
            "password": password,
            "name": name
        }
        response = requests.patch(Urls.UPDATE_DATA_USER, data = updated_data, headers = headers)
        return {"response_json": response.json(), "status_code": response.status_code}


    @staticmethod
    def get_ingredients(access_token):
        headers = {"Authorization": access_token}

        response = requests.get(Urls.INGREDIENTS, headers = headers)
        ingredients = []
        for ingredient in response.json()['data']:
            ingredients.append(ingredient['_id'])
        return ingredients

    @staticmethod
    def create_order(access_token, ingredients):
        headers = {"Authorization": access_token}

        data = {
            "ingredients": ingredients
        }

        response = requests.post(Urls.ORDER, headers = headers, data = data)
        result = { "status_code": response.status_code }
        try:
           result["response_json"] = response.json()
        except:
            pass

    @staticmethod
    def get_orders_for_user(access_token):
        headers = {"Authorization": access_token}

        response = requests.get(Urls.ORDER, headers=headers)
        return {"response_json": response.json(), "status_code": response.status_code}


