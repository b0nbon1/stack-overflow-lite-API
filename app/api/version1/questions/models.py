from flask import Flask
from datetime import datetime


# Create some test data for our catalog in the form of a list of dictionaries.
questions = [
    {"id": "1",
     "author": "bon",
     "title": "sql and c# ",
     "description": "How to Validate Where Expression in MS SQL Stored Procedure(Identify SQL Injection) or from C#",
     "tag": "c#, sql",
     "date": "15th december 2018"},
    {"id": "2",
     "author": "bonbon",
     "title": "java.sql.SQLException",
     "description": "java.sql.SQLException: No suitable driver in android studio",
     "tag": "android",
     "date": "16th december 2018"},
]


class Questions():
    def __init__(self):
        self.questions = questions

    def ask_question(self, author, title, description, tag):
        new_question = {
            "id": str(len(self.questions) + 1),
            "title": title,
            "description": description,
            "tag": tag,
            "author": author,
            "date": datetime.now()
        }
        self.questions.append(new_question)
        return self.questions