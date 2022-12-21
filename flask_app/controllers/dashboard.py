from datetime import date
from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.user import User
from flask_app.models.post import Equipment
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)
@app.route('/dashboard')
def dashboard():
    id = session['user']
    data={'id': id}
    user = User.get_one(data)
    return render_template('dashboard.html', user=user)