import os
from flask import render_template, url_for, redirect
from portfolio import db, app
from portfolio.model import credencials
from portfolio.form import RegistrationForm, LoginForm

@app.context_processor
def override_url_for():
    return dict(url_for=dated_url_for)

def dated_url_for(endpoint, **values):
    if endpoint == 'static':
        filename = values.get('filename', None)
        if filename:
            file_path = os.path.join(app.root_path,
                                 endpoint, filename)
            values['q'] = int(os.stat(file_path).st_mtime)
    return url_for(endpoint, **values)

@app.route("/register", methods=["POST", "GET"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = credencials(username=form.username.data, password=form.password.data)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('login'))
    return render_template("register.html", form=form)

@app.route("/")
@app.route("/login", methods=["POST", "GET"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = credencials.query.filter_by(username=form.username.data, password=form.password.data).first()
        if user:
            return redirect(url_for('home'))
    return render_template("login.html", form=form)

@app.route("/home", methods=["POST", "GET"])
def home():
    user = credencials.query.all()
    return render_template("home.html", user=user)

@app.route("/remove", methods=["POST", "GET"])
def remove():
    credencials.query.delete()
    db.session.commit()
    return redirect(url_for('login'))


