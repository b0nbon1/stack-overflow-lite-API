from flask import Flask, abort, jsonify
from werkzeug.security import check_password_hash, generate_password_hash


Users = [
    {
        "id": 1,
        "username": "bonbon",
        "email": "django@gmail.com",
        "password": generate_password_hash("bonvic")
    },
    {
        "id": 2,
        "username": "bon",
        "email": "flasky@gmail.com",
        "password": generate_password_hash("passpass")
    },
    {
        "id": 3,
        "username": "test",
        "email":"test@test.com",
        "password": generate_password_hash("testpytest")
    }
]


class User():

    def __init__(self, username, email, password):
        self.user_id = str(len(Users) + 1)
        self.email = email
        self.username = username
        self.password = password

    def register_user(self):
        new_user = {
            "id": self.user_id,
            "username": self.username,
            "email": self.email,
            "password": self.password
        }

        Users.append(new_user)
        return Users

    def get_user(username):
        user = [
            user for user in Users if user['username'] == username]
        return user

    def del_user(self, id):
        for user in Users:
            if (user['id'] == id):
                Users.remove(user)
                return Users
            return jsonify({'message': 'user not found'}), 404
