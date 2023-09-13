from zaqat import db

class Gampong(db.Model):
    Kode_Gampong = db.Column(db.String(5), primary_key=True)
    Nama_Gampong = db.Column(db.String(15), nullable=False)
    Kecamatan = db.Column(db.String(20), nullable=False)
    Dusun = db.Column(db.String(15), nullable=False)
    NIK = db.Column(db.String(16), nullable=False)
    Nama = db.Column(db.String(50), nullable=False)
    Email = db.Column(db.String(50), nullable=False)
    Nomor_HP = db.Column(db.String(13), nullable=False)
    Username = db.Column(db.String(20), nullable=False)
    Password = db.Column(db.String(20), nullable=False)
    
    def __repr__(self):
        return '<Gampong {}>' .format(self.name)