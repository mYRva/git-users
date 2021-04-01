from flaskr import db
 

class users(db.Model):
    id          = db.Column(db.Integer, primary_key=True)
    login       = db.Column(db.String(10), nullable=True)
    avatar_url  = db.Column(db.String(500),nullable=True)
    tipo        = db.Column(db.String(20), nullable=True )
    profile_url = db.Column(db.String(500), nullable=True)
 
    def __repr__(self):
        return f"'{self.id}','{self.login}','{self.avatar_url}','{ self.tipo }','{self.profile_url}'"

 