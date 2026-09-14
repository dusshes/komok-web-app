from app import db
from datetime import datetime, timedelta

class EmailVerificationCode(db.Model):
    __tablename__ = 'email_verification_codes'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    code_hash = db.Column(db.String(255), nullable=False)
    expires_at = db.Column(db.DateTime, nullable=False, default=lambda: datetime.utcnow() + timedelta(minutes=15))
    
    def is_expired(self):
        return datetime.utcnow() > self.expires_at
