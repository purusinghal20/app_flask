from app import app

@app.route("/")
def index():
    return "<h1> Home Page </h1>"

@app.route("/about")
def dash():
    return "<h1> About us </h1>"