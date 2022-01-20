from flask import Flask, render_template, flash, request, redirect, url_for, jsonify, Blueprint
from datetime import datetime 
from werkzeug.security import generate_password_hash, check_password_hash 
from datetime import date
from flask_login import UserMixin, login_user, LoginManager, login_required, logout_user, current_user
import uuid as uuid
from flask_cors import CORS
import os
from dotenv import dotenv_values
loc = os.path.join(os.path.dirname(os.path.realpath(__file__)).split('src')[0],'.env')
os_config = dotenv_values(loc)

from Session import Session
from Database.db_model import USER
Login = Flask(__name__)
CORS(Login)
# Login = Blueprint('Login', __name__)
login_manager = LoginManager()
login_manager.init_app(Login)
login_manager.login_view = 'login'
Login.config['SECRET_KEY'] = os_config['LOGIN_SECRET_KEY']
Login.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
Session =Session()

@Login.route('/register', methods =["POST"])
def register():
    Email = request.json["Email"]
    Password = request.json["Password"]
    Name = request.json["Name"]
    Age = request.json["Age"]
    Birthday = request.json["Birthday"]
    Phone = request.json["Phone"]
    City = request.json["City"]
    Country = request.json["Country"]
    user = Session.query(USER).filter_by(Email=Email).first()
    if user:
        return jsonify({"message":f"User already exists."}), 409
    else:
        new_password = generate_password_hash(Password, "sha256")
        user = USER(Name = Name, Age = int(Age), Birthday=Birthday, Email=Email,Phone = Phone, Country = Country, Password = new_password)
        Session.add(user)
        Session.commit()
        return jsonify({"message":f"User {Name} has been successfully created.", "User_ID":user.User_ID}), 200


@Login.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.json["Email"]
        password = request.json["Password"]
        user = Session.query(USER).filter_by(Email=username).first()
        if user:
            # Check the hash
            if check_password_hash(user.Password, password):
                login_user(user)
                return jsonify({"message":f"Logged in as {user.Name}.", "User_ID":user.User_ID}), 200
            else:
                return jsonify({"message":f"Password Error.", "User_ID":user.User_ID}), 401
        else:
            return jsonify({"message":"User does not exist.", "User_ID":"-1"}), 404
    return jsonify({"message": "Please log in.", "User_ID":"-1"}), 200


@Login.route('/dashboard', methods=['GET', 'POST'])
@login_required
def dashboard():
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




if __name__ == '__main__':
    Login.run(debug=True,host='localhost', port=5000)