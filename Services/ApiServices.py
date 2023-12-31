from Services.Endpoints import endpoints
import requests
import json

class ApiServices:

    def create_user(self, username, password):
        payload = {
            'userName': username,
            'password': password
        }
        response = requests.post(f"{endpoints.BASE_URL}{endpoints.ACCOUNT}{endpoints.USER}", data=payload)
        return response

    def generate_token(self, username, password):
        payload = {
            'userName': username,
            'password': password
        }
        response = requests.post(f"{endpoints.BASE_URL}{endpoints.ACCOUNT}{endpoints.GENERATE_TOKEN}", data=payload)
        return response

    def get_all_books(self):
        response = requests.get(f"{endpoints.BASE_URL}{endpoints.BOOKSTORE}{endpoints.BOOKS}")
        return response

    def post_book(self, userid, token, isbn):
        headers = {
            "accept": "application/json",
            "Content-Type": "application/json",
            "Authorization": "Bearer " + token
        }
        payload = {
            "userId": userid,
            "collectionOfIsbns": [
                {
                    "isbn": isbn
                }
            ]
        }

        json_payload = json.dumps(payload)

        response = requests.post(f"{endpoints.BASE_URL}{endpoints.BOOKSTORE}{endpoints.BOOKS}",
                                 data=json_payload,
                                 headers=headers)
        return response


apiServices = ApiServices()
