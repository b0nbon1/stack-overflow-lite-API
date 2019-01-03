[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)  [![Build Status](https://travis-ci.org/b0nbon1/stack-overflow-lite-API.svg?branch=develop)](https://travis-ci.org/b0nbon1/stack-overflow-lite-API)

# stack-overflow-lite-API

This is an api that enables stack overflow functionality
## The following are API endpoints enabling one to: 
- Get all questions.
- Get a question.
- Post a question.
- Post an answer to a question.

## Here is a list of the functioning endpoints

| EndPoint                              | Functionality                    |
| :---                                  |     :---:                        |   
| POST /auth/signup                     | register users       |  
| POST /auth/login | login user         |  
| GET /questions                        | Fetch all questions           |  
| GET /questions/< questionId >           | Fetch a specific question       |  
| POST /questions                       | Post a question                 | 
| Delete /questions/< questionId >               | Delete a question              | 
| POST /questions/< questionId >/answers              | Post an answer to a question             |  
| PUT /questions/< questionId >/answers/< answerId >               | Mark an answer as accepted or update an answer.|  
  
## Extra endpoints include 
* comments to add

## Testing the endpoints

* Install python then using pip instal .. install flask
* clone the repo
* Ensure that postman is installed
* From your terminal locate the repo and run: python run.py
* open postman and test the endpoint

## Setting up and how to start the application

* Install python then using pip instal .. install flask
* clone the repo
* From your terminal Ensure that the virtual environment is activated
* From the terminal locate the repo and run: python run.py

## Technology used

* Python 3.6
* Flask framework 

# Written by: Bonvic Bundi
#### Copyright © Andela 2018 

