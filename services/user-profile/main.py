from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from dotenv import load_dotenv
from model import db, UserProfile
from prometheus_flask_exporter import PrometheusMetrics

load_dotenv()

app = Flask(__name__)

metrics = PrometheusMetrics(app)

app.config.from_object('config.Config')

db = SQLAlchemy(app)
migrate = Migrate(app, db)

@app.route('/user/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = UserProfile.query.get(user_id)
    if user:
        return jsonify(user.to_dict()), 200
    return jsonify({'message': 'User not found'}), 404

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(host='0.0.0.0', port=5001)
