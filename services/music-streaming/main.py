from flask import Flask, jsonify
from prometheus_flask_exporter import PrometheusMetrics
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from model import db, Stream

app = Flask(__name__)

metrics = PrometheusMetrics(app)

app.config.from_object('config.Config')

db = SQLAlchemy(app)
migrate = Migrate(app, db)

@app.route('/stream/<int:track_id>', methods=['GET'])
def stream_music(track_id):
    stream_data = {"track_id": track_id, "status": "streaming"}
    return jsonify(stream_data)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(host='0.0.0.0', port=5000)
