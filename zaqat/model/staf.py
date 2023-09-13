from zaqat import db
from zaqat.model.admin import Admin

class Staf(db.Model):
    NIK = db.Column(db.String(16), primary_key=True)
    Nama = db.Column(db.String(50), nullable=False)
    Email = db.Column(db.String(50), nullable=False)
    Nomor_HP = db.Column(db.String(13), nullable=False)
    Username = db.Column(db.String(20), nullable=False)
    Password = db.Column(db.String(20), nullable=False)
    Kecamatan = db.Column(db.String(20), nullable=False)
    Gampong = db.Column(db.String(15), nullable=False)
    Kode_Gampong = db.Column(db.String(5), nullable=False)
    Dusun = db.Column(db.String(15), nullable=False)
    Admin =  db.Column(db.BigInteger, db.ForeignKey(Admin.ID_Admin))
    
    def __repr__(self):
        return '<Staf {}>' .format(self.name)