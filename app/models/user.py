from app import db
from datetime import datetime

class User(db.Model):
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=True)
    name = db.Column(db.String(100), nullable=False)
    oauth_provider = db.Column(db.String(50), nullable=True)
    oauth_id = db.Column(db.String(100), nullable=True)
    is_admin = db.Column(db.Boolean, default=False)
    
    # Для обычных пользователей
    country_id = db.Column(db.Integer, db.ForeignKey('countries.id'), nullable=True)
    city_id = db.Column(db.Integer, db.ForeignKey('cities.id'), nullable=True)
    
    # Контакты
    whatsapp = db.Column(db.String(50), nullable=True)
    telegram = db.Column(db.String(100), nullable=True)
    zalo = db.Column(db.String(50), nullable=True)
    max = db.Column(db.String(100), nullable=True)
    preferred_contact = db.Column(db.String(20), default='email')
    
    payout_details = db.Column(db.Text, nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    # Связи
    # Для администраторов связь с городами через admin_city_assignments
    admin_cities = db.relationship('City', secondary='admin_city_assignments', backref='admins')
