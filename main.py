from flask import Flask,render_template

app=Flask(__name__)

@app.route("/")
def welcome():
    return "<html><h1>Welcome to the flask course</h1></html>"
@app.route("/index")
def index():
    return render_template("index.html") #go inside template page to look for index.html

@app.route("/about")
def about():
    return render_template("about.html")

if __name__=="__main__": #From here execution will start
    app.run(debug=True) #entire flask app is going to run,debug=True so i don't have to restart the server when something is added