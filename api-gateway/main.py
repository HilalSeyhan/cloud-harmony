from flask import Flask
from flask_restful import Api
from dotenv import load_dotenv
from prometheus_flask_exporter import PrometheusMetrics
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from routes import initialize_routes

load_dotenv()

app = Flask(__name__)

metrics = PrometheusMetrics(app)

app.config.from_object('config.Config')

db = SQLAlchemy(app)
migrate = Migrate(app, db)

api = Api(app)
initialize_routes(api)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
