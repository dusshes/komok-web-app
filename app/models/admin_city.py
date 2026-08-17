from app import db

class AdminCityAssignment(db.Model):
    __tablename__ = 'admin_city_assignments'
    
    admin_id = db.Column(db.Integer, db.ForeignKey('users.id', ondelete='CASCADE'), primary_key=True)
    city_id = db.Column(db.Integer, db.ForeignKey('cities.id', ondelete='CASCADE'), primary_key=True)
