from app import app
from flask import render_template, request
from app.models import model, formopener


@app.route("/results", methods=['GET', 'POST'])
def reverseit():
    userdata=dict(request.form)
    word=str(userdata["word"])
    if request.method=="GETS":
        return "You are at the wrong place."
    else:
        return render_template('results.html', word=model.reverse(word))

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')
