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
    choice = userdata['choice']
    print(choice)
    print(type(choice))
    genre = ""
    game = ""
    if choice == '1':
        game = "Witcher 3"
        genre = "RPG"
    if choice == '2':
        game = "FIFA"
        genre = "Sports"
    if choice == '3':
        game = "CoD"
        genre = "MMO"
    genre = model.concatenate(genre)
    print(game)
    return render_template("results.html", game = game, genre = genre)
