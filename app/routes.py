from flask import Flask
from flask import render_template
# from app import app

app = Flask(__name__)

@app.route('/')
def index():
    fake_logins = [{"username": "rollarskates44", "password": "wheelsRus"}, {"username": "soccermom1982", "password": "goalgoalgoal123"}, {"username": "scienceperson17", "password": "nitric-acid-KNO3"}]
    authors = "Flask"
    return render_template("index.html", logs=fake_logins, author=authors)

@app.route('/about')
def about():
    me = "David Ekunno"
    return render_template("about-us.html", name=me)

@app.route('/games')
def games():
    return 'The Games page'

# if __name__ == '__main__':
#     app.run()