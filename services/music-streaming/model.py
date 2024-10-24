from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Stream(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)
    song_id = db.Column(db.Integer, nullable=False)
    timestamp = db.Column(db.DateTime, default=db.func.current_timestamp())
    duration_listened = db.Column(db.Integer)
