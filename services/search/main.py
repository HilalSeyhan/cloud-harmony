from flask import Flask, jsonify, request
from elasticsearch import Elasticsearch
from prometheus_flask_exporter import PrometheusMetrics
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from model import db, Search

app = Flask(__name__)

metrics = PrometheusMetrics(app)

app.config.from_object('config.Config')

db = SQLAlchemy(app)
migrate = Migrate(app, db)

es = Elasticsearch(['http://elasticsearch:9200'])

@app.route('/search', methods=['GET'])
def search():
    query = request.args.get('query', '')
    result = es.search(index="music", body={"query": {"match": {"title": query}}})
    return jsonify(result['hits']['hits'])

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(host='0.0.0.0', port=5000)
