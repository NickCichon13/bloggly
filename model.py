from flask_sqlalchemy import SQLAlchemy
import datetime


db =SQLAlchemy()

DEFAULT_IMAGE_URL = "https://www.freeiconspng.com/uploads/icon-user-blue-symbol-people-person-generic--public-domain--21.png"

def connect_db(app):
    db.app = app
    db.init_app(app)


class User(db.Model):
    
    __tablename__ = "users"

    id = db.Column(db.Integer,primary_key = True, autoincrement = True)
    first_name = db.Column(db.Text(20), nullable = False, unique = True)
    last_name = db.Column(db.Text(20), nullable = False, unique = True)
    image_url = db.Column(db.Text, nullable = False, default = DEFAULT_IMAGE_URL)
    
    posts = db.relationship("Post", backref="user", cascade="all, delete-orphan")
class Post(db.Model):

    __tablename__ = "Posts"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.Text, nullable = False)
    content = db.Column(db.Text, nullable = False)
    created_at = db.Column(db.DateTime, nullable = False, default = datetime.datetime.now)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
