import os

class Config:
    DB_USER = os.getenv('DB_USER', 'bbuser')
    DB_PASSWORD = os.getenv('DB_PASSWORD', 'bbuser')
    DB_HOST = os.getenv('DB_HOST', 'postgres-db')
    DB_PORT = os.getenv('DB_PORT', '5432')
    DB_NAME = os.getenv('DB_NAME', 'music_streaming_db')

    SQLALCHEMY_DATABASE_URI = f'postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'

    STREAM_QUALITY = os.getenv('STREAM_QUALITY', 'high')
