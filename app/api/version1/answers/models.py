from datetime import datetime


# Create some test data for our catalog in the form of a list of dictionaries.
answers = [
    {"id": "1",
     "question_id": "1",
     "author": "bon",
     "accepted": False,
     "ans": "How to Validate Where Expression in MS SQL Stored Procedure(Identify SQL Injection) or from C#",
     "date": "15th december 2018"},
    {"id": "2",
     "question_id": "1",
     "author": "bonbon",
     "accepted": False,
     "ans": "java.sql.SQLException: No suitable driver in android studio",
     "date": "16th december 2018"}
]


class Answer():
    def __init__(self):
        self.answers = answers

    def post_answer(self, author, ans, question_id):
        default = False
        new_answer = {
            "id": str(len(self.answers) + 1),
            "question_id": question_id,
            "ans": ans,
            "accepted": default,
            "author": author,
            "date": datetime.now()
        }
        self.answers.append(new_answer)
        return self.answers
