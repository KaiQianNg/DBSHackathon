from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()


class USERS(db.Model,UserMixin):
	User_ID = db.Column(db.Integer, primary_key=True)
	Name = db.Column(db.String(100), nullable=False)
	Age = db.Column(db.Integer, nullable=False)
	Birthday = db.Column(db.String(10), nullable=False)
	Phone = db.Column(db.String(50), nullable=False)
	City = db.Column(db.String(100), nullable=False)
	Country = db.Column(db.String(100), nullable=False)
    Password = db.Column(db.String(300), nullable=False)
class LIKED_POST(db.Model):
	Ref_Num = db.Column(db.Integer, primary_key=True)
    User_ID  = db.Column(db.Integer, nullable=False)
    Post_ID  = db.Column(db.Integer, nullable=False)
class POST(db.Model):
	Ref_Num = db.Column(db.Integer, primary_key=True)
    Post_ID  = db.Column(db.Integer, nullable=False)
    User_ID  = db.Column(db.Integer, nullable=False)
	Post_Title = db.Column(db.String(100), nullable=False)
	Post_Description = db.Column(db.String(500), nullable=False)
	Post_image = db.Column(db.String(500), nullable=False)
class POST_COMMENT(db.Model):
	Ref_Num = db.Column(db.Integer, primary_key=True)
    User_ID  = db.Column(db.Integer, nullable=False)
    Post_ID  = db.Column(db.Integer, nullable=False)
	Post_Title = db.Column(db.String(100), nullable=False)
	Post_Description = db.Column(db.String(500), nullable=False)
	Post_image = db.Column(db.String(500), nullable=False)
