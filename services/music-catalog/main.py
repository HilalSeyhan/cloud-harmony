from flask import Flask, jsonify
from prometheus_flask_exporter import PrometheusMetrics
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from model import db, Song

app = Flask(__name__)

metrics = PrometheusMetrics(app)

app.config.from_object('config.Config')

db = SQLAlchemy(app)
migrate = Migrate(app, db)

@app.route('/catalog', methods=['GET'])
def get_catalog():
    catalog = [
        {"track_id": 1, "title": "Track One", "artist": "Artist One"},
        {"track_id": 2, "title": "Track Two", "artist": "Artist Two"}
    ]
    return jsonify(catalog)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(host='0.0.0.0', port=5000)
