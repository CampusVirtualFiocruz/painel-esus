import json

from src.env.conf import getenv


def create_user(user, password):
    return {
        "login": user,
        "password": password,
        "data": {
            "username": user,
            "cns": "0000000000",
            "uf": "",
            "municipio": "",
            "profiles": ["admin"],
        },
    }

def get_users_list():
    users = getenv("ACCESS_LIST", '[]', False)
    return json.loads(users)

users_list = get_users_list()
if len(users_list) > 0: 
    users = [
        create_user(user["user"], user["password"]) for user in users_list
    ]
else:
    users = []
