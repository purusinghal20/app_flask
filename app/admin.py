from app import app

@app.route("/admin/dash")
def admin_dash():
    return "<h1> Admin dash </h1>"

@app.route("/admin/profile")
def admin_profile():
    return "<h1> Admin profile </h1>"