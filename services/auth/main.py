from flask import Flask, jsonify, request
from flask_jwt_extended import JWTManager, create_access_token
from prometheus_flask_exporter import PrometheusMetrics
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from model import db, TokenBlocklist

app = Flask(__name__)

metrics = PrometheusMetrics(app)

app.config.from_object('config.Config')

db.init_app(app)
migrate = Migrate(app, db)

app.config['JWT_SECRET_KEY'] = 'WCZN_WQ9-rVdYWkeE6e60Pa49wqMNtnQgJFowHXw114'
jwt = JWTManager(app)

@app.route('/auth', methods=['POST'])
def authenticate():
    username = request.json.get('username', None)
    password = request.json.get('password', None)
    
    if username == 'admin' and password == 'admin_password':
        access_token = create_access_token(identity=username)
        return jsonify(access_token=access_token), 200
    
    return jsonify({"msg": "Invalid credentials"}), 401

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
