from flask import Flask, abort, jsonify, make_response, request, Blueprint
from app.api.version1.questions.models import Questions, questions

quest = Blueprint('questions', __name__, url_prefix='/questions')


@quest.route('/', methods=['GET'])
def fetch_all_qustions():
    if len(questions) == 0:
        return make_response(jsonify({"message": "no available questions right now"})), 404
    return make_response(jsonify(questions)), 200


@quest.route('/<int:question_id>', methods=['GET'])
def get_question(question_id):
    question = [
        question for question in questions if question['id'] == question_id]
    if len(question) == 0:
        abort(404)
    return make_response(jsonify(question)), 200

@quest.route('/new_question', methods=['POST'])
def ask_question():
    data = request.get_json()
    if not data:
        abort(400)

    title = data["title"]
    description = data["description"]
    tag = data["tag"]
    author = data["author"]

    ask = Questions().ask_question(author, title, description, tag)    
    return make_response(jsonify(ask)), 200