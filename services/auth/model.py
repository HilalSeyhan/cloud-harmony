from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class TokenBlocklist(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    jti = db.Column(db.String(36), nullable=False)  # JWT ID
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
