import os

from flask import Flask, jsonify
from instance.config import configuration


def create_app(config):
    '''creating app and configure the apps'''

    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(configuration)
    app.secret_key = os.urandom(24)

    from .api.version1.auth.views import auth
    app.register_blueprint(auth)

    from .api.version1.questions.views import quest
    app.register_blueprint(quest)

    # a simple page that says hello to taste the app

    @app.route('/hello', methods=['GET'])
    def hello():
        return jsonify({"message": "hello, world"})
    return app
