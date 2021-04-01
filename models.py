from flask_login import UserMixin
from flaskr import db, login_manager

class User(db.Model, UserMixin):
    #id,login,avatar_url, type, profile_url
    id          = db.Column(db.Integer, primary_key=True)
    login       = db.Column(db.String(10), unique=True, nullable=False)
    avatar_url  = db.Column(db.String(500), unique=True, nullable=False)
    tipo        = db.Column(db.String(20), nullable=False )
    profile_url = db.Column(db.String(500), nullable=False)
 
    def __repr__(self):
        return f"User('{self.id}', '{self.login}', '{self.avatar_url}', '{ self.tipo }', '{self.profile_url}')"
