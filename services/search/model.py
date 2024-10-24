from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Search(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)
    query = db.Column(db.String(200), nullable=False)  # Kullanıcının yaptığı arama sorgusu
    timestamp = db.Column(db.DateTime, default=db.func.current_timestamp())
