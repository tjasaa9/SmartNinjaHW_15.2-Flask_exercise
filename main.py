#Imported Flask into a Python file
from flask import Flask, render_template

#A new Flask app object
app = Flask(__name__)


#Controllers/Handlers
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/about")
def about_me():
    return render_template("about.html")

@app.route("/portfolio")
def portfolio():
    return render_template("portfolio.html")


@app.route("/portfolio/fakebook")
def fakebook():
    return render_template("fakebook.html")

@app.route("/portfolio/boogle")
def boogle():
    return render_template("boogle.html")

@app.route("/portfolio/hairsalon")
def hairsalon():
    return render_template("hairsalon.html")


if __name__ == '__main__':
   # app.run(use_reloader=True)
    app.run(port=4456, use_reloader=True)
