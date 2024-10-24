#jinja2 Template Engine
'''
{{ }} expressions to print output in html
{%...%} conditions, for loops
{#...#} this is for comments

'''

from flask import Flask,render_template,request,redirect,url_for

app=Flask(__name__)

@app.route("/")
def welcome():
    return "<html><h1>Welcome to the flask course</h1></html>"
@app.route("/index",methods=['GET'])
def index():
    return render_template("index.html") #go inside template page to look for index.html

@app.route("/about")
def about():
    return render_template("about.html")



@app.route("/submits",methods=['POST','GET'])
def submits():
    if request.method=='POST':
        name=request.form['name']
        return f"Hello {name}!"
    return render_template('form.html')

#variable rule
@app.route('/success/<int:score>')
def success(score):
    res=""
    if score>=50:
        res="PASS"
    else:
        res="FAIL"
    return render_template("result.html",results=res)


#variable rule with jinja2 
@app.route('/successres/<int:score>')
def successres(score):
    res=""
    if score>=50:
        res="PASS"
    else:
        res="FAIL"
    exp={'score':score,'res':res}
    return render_template("result1.html",results=exp)
@app.route('/fail/<int:score>')
def fail(score):
    return render_template('result.html')




##Dynamic URL
@app.route('/getresults',methods=['POST','GET']) #app route wala naam likhna hai form ke action mein
def getresults():
    total_score=0
    if request.method=='POST':
        science=float(request.form['science'])
        maths=float(request.form['maths'])
        c=float(request.form['c'])
        data_science=float(request.form['datascience'])

        total_score=(science+maths+c+data_science)/4
    else:
        return render_template('getresults.html')#when /getresults--->else block--->if block--->return redirect1,/
    return redirect(url_for('successres',score=total_score))




if __name__=="__main__": #From here execution will start
    app.run(debug=True) #entire flask app is going to run,debug=True so i don't have to restart the server when something is added