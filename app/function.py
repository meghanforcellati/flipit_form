# reverseit function, 1 parameter, string, and return in reverse
from flask import render_template, request, redirect
from app import app
from app.models import model, formopener

@app.route("/results", methods=['GET', 'POST'])
def reverseit():
    userdata=request.form
    word=str(request["word"])
    if request.method=="GETS":
        return "You are at the wrong place."
    else:
        return render_template('results.html', word=word[:-1])

@app.route('/index')
def index():
    return render_template('index.html')