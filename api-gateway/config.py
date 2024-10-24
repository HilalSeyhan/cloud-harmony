import os

class Config:
    USER_PROFILE_SERVICE_URL = os.getenv('USER_PROFILE_SERVICE_URL', 'http://user-profile:5001')
    AUTH_SERVICE_URL = os.getenv('AUTH_SERVICE_URL', 'http://auth:5002')
    MUSIC_STREAMING_SERVICE_URL = os.getenv('MUSIC_STREAMING_SERVICE_URL', 'http://music-streaming:5003')
    MUSIC_CATALOG_SERVICE_URL = os.getenv('MUSIC_CATALOG_SERVICE_URL', 'http://music-catalog:5004')
    SEARCH_SERVICE_URL = os.getenv('SEARCH_SERVICE_URL', 'http://search:5005')
