from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy
from dotenv import dotenv_values
loc = os.path.join(os.path.dirname(os.path.realpath(__file__)).split('src')[0],'.env')
os_config = dotenv_values(loc)

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] =  os_config['SQLALCHEMY_DATABASE_URI']
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
class USERS(db.Model,UserMixin):
	__tablename__ = 'USERS'
	User_ID = db.Column(db.Integer, primary_key=True)
	Name = db.Column(db.String(100), nullable=False)
	Age = db.Column(db.Integer, nullable=False)
	Birthday = db.Column(db.String(10), nullable=False)
	Email = db.Column(db.String(100), nullable=False)
	Phone = db.Column(db.String(50), nullable=False)
	City = db.Column(db.String(100), nullable=False)
	Country = db.Column(db.String(100), nullable=False)
	Password = db.Column(db.String(300), nullable=False)
class LIKED_POST(db.Model):
	__tablename__ = 'LIKED_POST'
	Ref_Num = db.Column(db.Integer, primary_key=True)
	User_ID  = db.Column(db.Integer, nullable=False)
	Post_ID  = db.Column(db.Integer, nullable=False)
class POST(db.Model):
	__tablename__ = 'POST'
	Post_ID  = db.Column(db.Integer, nullable=False, primary_key=True)
	User_ID  = db.Column(db.Integer, nullable=False)
	Post_Title = db.Column(db.String(100), nullable=False)
	Post_Description = db.Column(db.String(500), nullable=False)
	Post_image = db.Column(db.String(500), nullable=False)
class POST_COMMENT(db.Model):
	__tablename__ = 'POST_COMMENT'
	Comment_ID = db.Column(db.Integer, primary_key=True)
	User_ID  = db.Column(db.Integer, nullable=False)
	Post_ID  = db.Column(db.Integer, nullable=False)
	Comment = db.Column(db.String(500), primary_key=True)

db.create_all()