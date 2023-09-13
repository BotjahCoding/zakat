from zaqat import db
from datetime import datetime


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), index=True, unique=True, nullable=False)
    #index ditujukan sebagai pengenal dan unique sebagai pembeda dengan yang lain
    password = db.Column(db.String(50), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    def __repr__(self):
        return '<User {}>'.format(self.name)
    