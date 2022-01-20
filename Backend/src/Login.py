from flask import Flask, render_template, flash, request, redirect, url_for
from datetime import datetime 
from werkzeug.security import generate_password_hash, check_password_hash 
from datetime import date
from flask_login import UserMixin, login_user, LoginManager, login_required, logout_user, current_user
import uuid as uuid
import os
from Session import Session
from Database.db_model import USERS

Login = Blueprint('Login', __name__)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'


@Login.route('/register', methods =["POST"])
def register():
    Email = request.form.get("Email")
    Password = request.form.get("Password")
    Name = request.form.get("Name")
    Age = request.form.get("Age")
    Birthday = request.form.get("Birthday")
    Phone = request.form.get("Phone")
    City = request.form.get("City")
    Country = request.form.get("Country")
    user = session.query(USERS).filter_by(Email=Email).first()

    if user:
        return {"message":f"User already exists."}, 409
    else:
        new_password = generate_password_hash(Password)
        user = USERS(Name = Name, Age = int(Age), Birthday=Birthday, Email=Email,Phone = Phone, Country = Country, Password = new_password)
        Session.add(user)
        Session.commit()
        return {"message":f"User {Name} has been successfully created."}, 200


@Login.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get("Email")
        password = request.form.get("Password")
        user = session.query(USERS).filter_by(Email=username).first()
        if user:
            # Check the hash
            if check_password_hash(user.Password, password):
                login_user(user)
                return {"message":f"Logged in as {user.Name}."}, 200
            else:
                return {"message":f"Password Error."}, 401
        else:
            return {"message":"User does not exist."}, 404
    return {"message": "Please log in"}, 200


@Login.route('/dashboard', methods=['GET', 'POST'])
@login_required
def dashboard():
	user = current_user.Email
	pass

@Login.route('/logout', methods=['GET', 'POST'])
@login_required
def logout():
	logout_user()
	return {"message":f"Logged out."}, 200