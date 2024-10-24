from flask import Flask

''' It creates an instance of the flask class,
which will be your WSGI(Web Server Gateway Interface) application.'''
##WSGI Application
app=Flask(__name__)


@app.route("/")
def welcome():
    return "Welcome to this best flask course.This should be an amazing course,"
@app.route("/index")
def index():
    return "Welcome to the index page"


if __name__=="__main__": #From here execution will start
    app.run(debug=True) #entire flask app is going to run,debug=True so i don't have to restart the server when something is added