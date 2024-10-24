import os

class Config:
    ES_HOST = os.getenv('ES_HOST', 'elasticsearch')
    ES_PORT = os.getenv('ES_PORT', '9200')

    ELASTICSEARCH_URL = f'http://{ES_HOST}:{ES_PORT}'
    
    DB_USER = os.getenv('DB_USER', 'bbuser')
    DB_PASSWORD = os.getenv('DB_PASSWORD', 'bbuser')
    DB_HOST = os.getenv('DB_HOST', 'postgres-db')
    DB_PORT = os.getenv('DB_PORT', '5432')
    DB_NAME = os.getenv('DB_NAME', 'search_db')

    SQLALCHEMY_DATABASE_URI = f'postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'
