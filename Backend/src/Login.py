from flask import Flask, render_template, flash, request, redirect, url_for, jsonify, Blueprint
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
login_manager.init_app(Login)
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
    user = Session.query(USERS).filter_by(Email=Email).first()
    if user:
        return {"message":f"User already exists."}, 409
    else:
        new_password = generate_password_hash(Password)
        user = USERS(Name = Name, Age = int(Age), Birthday=Birthday, Email=Email,Phone = Phone, Country = Country, Password = new_password)
        Session.add(user)
        Session.commit()
        return jsonify({"message":f"User {Name} has been successfully created.", "User_ID":user.User_ID}), 200


@Login.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get("Email")
        password = request.form.get("Password")
        user = Session.query(USERS).filter_by(Email=username).first()
        if user:
            # Check the hash
            if check_password_hash(user.Password, password):
                login_user(user)
                return jsonify({"message":f"Logged in as {user.Name}.", "User_ID":user.User_ID}), 200
            else:
                return jsonify({"message":f"Password Error.", "User_ID":user.User_ID}), 401
        else:
            return jsonify({"message":"User does not exist.", "User_ID":user.User_ID}), 404
    return jsonify({"message": "Please log in."}), 200


@Login.route('/dashboard', methods=['GET', 'POST'])
@login_required
def dashboard():
	user = current_user.Email
	return jsonify({"message":f"Hi {current_user.Name}!", "User_ID":current_user.User_ID}), 200


@Login.route('/dashboard/delete', methods=['GET', 'POST'])
@login_required
def delete_user():
    user = current_user.Email
    Session.delete(current_user)
    Session.commit()

    return jsonify({"message":f"User deleted.", "User_ID":user.User_ID}), 200

@Login.route('/logout', methods=['GET', 'POST'])
@login_required
def logout():
    current_id = current_user.User_ID 
    logout_user()
    return jsonify({"message":f"Logged out.", "User_ID":current_id}), 200