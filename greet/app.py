from flask import Flask
app = Flask(__name__)


@app.route('/welcome')
def display_welcome():
    """This function displays a welcome message when a GET request is submitted to the '/welcome' route"""
    return 'welcome'


@app.route('/welcome/home')
def display_welcome_home():
    """This function displays a welcome home message when a GET request is submitted to the '/welcome' route"""
    return 'welcome home'


@app.route('/welcome/back')
def display_welcome_back():
    """This function displays a welcome back message when a GET request is submitted to the '/welcome' route"""
    return 'welcome back'
