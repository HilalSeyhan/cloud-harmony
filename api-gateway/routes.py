from flask import request, jsonify
from flask_restful import Api, Resource
import requests
from config import Config

def initialize_routes(api: Api):
    api.add_resource(UserProfile, '/api/user-profile/<string:user_id>')
    api.add_resource(Auth, '/api/auth')
    api.add_resource(MusicStream, '/api/music-stream')
    api.add_resource(MusicCatalog, '/api/music-catalog')
    api.add_resource(Search, '/api/search')

class UserProfile(Resource):
    def get(self, user_id):
        response = requests.get(f'{Config.USER_PROFILE_SERVICE_URL}/user/{user_id}')
        return jsonify(response.json())

class Auth(Resource):
    def post(self):
        data = request.get_json()
        response = requests.post(f'{Config.AUTH_SERVICE_URL}/login', json=data)
        return jsonify(response.json())

class MusicStream(Resource):
    def get(self):
        response = requests.get(f'{Config.MUSIC_STREAMING_SERVICE_URL}/stream')
        return jsonify(response.json())

class MusicCatalog(Resource):
    def get(self):
        response = requests.get(f'{Config.MUSIC_CATALOG_SERVICE_URL}/catalog')
        return jsonify(response.json())

class Search(Resource):
    def get(self):
        query = request.args.get('query')
        response = requests.get(f'{Config.SEARCH_SERVICE_URL}/search?q={query}')
        return jsonify(response.json())