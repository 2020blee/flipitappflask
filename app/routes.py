from app import app
from flask import render_template, request
from app.models import model, formopener

#Flask interface
@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")

@app.route('/results', methods = ["GET", "POST"])
def results():
    userdata = dict(request.form)
    print(userdata)
    nickname = userdata['nickname']
    output = model.flipit(nickname)
    return render_template("results.html", output = output)
