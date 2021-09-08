from flask import Flask

app = Flask(__name__)

@app.get('/welcome')
def say_welcome():
    return "<h1>Welcome!</h1>"

@app.get('/welcome/home')
def say_welcome_home():
    return "<h1>Welcome Home!</h1>"

@app.get('/welcome/back')
def say_welcome_back():
    return "<h1>Welcome Back!</h1>"