import os

from flask import Flask, jsonify
from instance.config import configuration


def create_app(config):
    '''creating app'''
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(configuration)
    app.secret_key = os.urandom(24)

    from .api.version1.auth.views import auth
    app.register_blueprint(auth)

    from .api.version1.questions.views import quest
    app.register_blueprint(quest)

    from .api.version1.answers.views import answ
    app.register_blueprint(answ)

    # a simple page that says hello

    @app.route('/hello')
    def hello():
        return jsonify({"message": "hello, world"})
    return app
