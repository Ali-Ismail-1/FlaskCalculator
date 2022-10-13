# Flask Calculator


## Introduction
Hi!
This is a Calculator App using Python Flask, Bootstrap CSS, and jQuery. 

## Summary
This calculator app stores your calculations in a stack until you press the '=' button.
Upon hitting the '=' button, the app will make an AJAX call and send the stack to Python Django via a http GET request. 
The GET request will make the calculation and send the result back to the html page is show it in the 'display' of the calculator.

### I've kept the requirements minimum for this project by using references to CDN urls for 
 - Bootstrap CSS
 - jQuery

## Requirements

### You will need the following packages to run the solution: 
- click==8.1.3
- colorama==0.4.5
- Flask==2.2.2
- importlib-metadata==5.0.0
- itsdangerous==2.1.2
- Jinja2==3.1.2
- MarkupSafe==2.1.1
- typing_extensions==4.4.0
- Werkzeug==2.2.2
- zipp==3.9.0


## Setup

### You can set up the project by running the following commands :D

#### Using git bash, run the following command:
git clone https://github.com/Ali-Ismail-1/FlaskCalculator.git

#### Install django if you do not have it already 
pip install Flask==2.2.2

#### Open the folder FlaskCalculator and run the following command to start the server:
python app.py

#### View the Calculator app using the following url:
http://127.0.0.1:5000/calculator/



## Reproduction

### Just in case you want to follow my set up steps from scratch, here's the commands I used in my terminal
- virtualenv flask_env
- flask_env\Scripts\activate
- pip install Flask
- python app.py
- pip freeze > requirements.txt
