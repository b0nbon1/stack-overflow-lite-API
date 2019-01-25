from flask import Flask, abort, jsonify, make_response, request, Blueprint
from werkzeug.security import check_password_hash, generate_password_hash
from app.api.version1.users.models import Users, User
from app.api.version1.users.utils import validators


auth = Blueprint('auth', __name__, url_prefix='/auth')


@auth.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data['username']
    email = data['email']
    password = data['password']
    confirm_password = data['confirm_password']

    # validators
    validator = validators(username, email, password)
    check_username = validator.validate_username()
    if check_username is False:
        return make_response(jsonify({"message": "invalid username"})), 400

    username_exist = validator.username_exists()

    if username_exist is True:
        return make_response(jsonify({"message": "username exists"})), 400

    check_email = validator.validate_email()

    if check_email is False:
        return make_response(jsonify({"message": "invalid email"})), 400

    check_password = validator.validate_password()

    if check_password is False:
        return make_response(jsonify({"message": "invalid password"})), 400

    if password == confirm_password:
        '''Add user to the data structure'''
        password = generate_password_hash(password)
        new_user = User(username, email, password)
        add_user = new_user.register_user()

        return make_response(jsonify({"message": "user successfull registered!"})), 200
    else:
        return make_response(
            jsonify({"message": "Passwords don't match"})), 400


@auth.route('/login', methods=['POST'])
def login():
    '''login a user to the platform'''
    data = request.get_json()
    username = data['username']
    password = data['password']

    user = User.get_user(username)
    if len(user) == 0:
            return make_response(jsonify({'message': 'user not found'}), 404)
    else:
        if check_password_hash(user[0]['password'], password):
            return make_response(jsonify({"message":
                                          "Successfully Logged In"}), 200)
        else:
            return jsonify({"message": "wrong password"}), 404
