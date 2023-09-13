from zaqat import db

class Admin(db.Model):
    ID_Admin = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    NIK = db.Column(db.String(16), nullable=False)
    Nama = db.Column(db.String(50), nullable=False)
    Username = db.Column(db.String(20), nullable=False)
    Password = db.Column(db.String(20), nullable=False)
    
    def __repr__(self):
        return '<Admin {}>' .format(self.name)