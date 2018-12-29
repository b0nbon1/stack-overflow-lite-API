from flask import Flask, abort, jsonify, make_response, request, Blueprint
from app.api.version1.answers.models import Answer, answers

answ = Blueprint('answers', __name__, url_prefix='/questions/<string:question_id>/answers')


@answ.route('/', methods=['GET'])
def fetch_all_qustions(question_id):
    answer = [
        answer for answer in answers if answer['question_id'] == question_id]
    if len(answer) == 0:
        return make_response(jsonify({"message": "no available answers for this question currently"})), 404
    return make_response(jsonify(answer)), 200


@answ.route('/<string:answer_id>', methods=['GET'])
def get_question(question_id, answer_id):
    answer = [
        answer for answer in answers if answer['question_id'] == question_id]
    if len(answer) == 0:
        return make_response(jsonify({"message": "no answers"})), 404
    ans = [
        ans for ans in answer if ans['id'] == answer_id]
    if len(ans) == 0:
        return make_response(jsonify({"message": "no such answer"})), 404
    return make_response(jsonify(ans)), 200


@answ.route('/new_answer', methods=['POST'])
def answer_question(question_id):
    data = request.get_json()
    if not data:
        abort(400)

    answer = data["answer"]
    quest_id = question_id
    author = data["author"]

    ask = Answer().post_answer(author, answer, quest_id)

    return make_response(jsonify(ask,{"message": "successful added"})), 200


@answ.route('/<string:answer_id>', methods=['DELETE'])
def delete_question(question_id, answer_id):
    answer = [
        answer for answer in answers if answer['question_id'] == question_id]
    if len(answer) == 0:
        return make_response(jsonify({"message": "no answers"})), 404

    # if question_id.isdigit():
    for ans in answer:
        if (answer_id) == ans["id"]:
            answer.remove(ans)
            return make_response(jsonify(answer, {"message": "answer deleted successful"})), 200
    return make_response(jsonify({"Message": "no answer"})), 404
    # return make_response(jsonify({"Message": "Invalid question id"})), 404


@answ.route('/<string:answer_id>', methods=['PUT'])
def update_question(question_id, answer_id):
    answer = [
        answer for answer in answers if answer['question_id'] == question_id]
    if len(answer) == 0:
        return make_response(jsonify({"message": "no answers"})), 404
    ans = [
        ans for ans in answer if ans['id'] == answer_id]
    if len(ans) == 0:
        return make_response(jsonify({"message": "no such answer"})), 404

    ans[0]["ans"] = request.json.get("ans", ans[0]["ans"])
    ans[0]["accepted"] = request.json.get("accepted", ans[0]["accepted"])
    return make_response(jsonify(ans, {"message": " succesful update the answer"})), 200
