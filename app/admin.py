from app import app
from flask import render_template

@app.route("/admin/dash")
def admin_dash():
    return render_template("admin/dash.html")

@app.route("/admin/profile")
def admin_profile():
    return "<h1> Admin profile </h1>"