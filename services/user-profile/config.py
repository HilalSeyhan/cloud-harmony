import os

class Config:
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY', 'WCZN_WQ9-rVdYWkeE6e60Pa49wqMNtnQgJFowHXw114')

    DB_USER = os.getenv('DB_USER', 'bbuser')
    DB_PASSWORD = os.getenv('DB_PASSWORD', 'bbuser')
    DB_HOST = os.getenv('DB_HOST', 'postgres-db')
    DB_PORT = os.getenv('DB_PORT', '5432')
    DB_NAME = os.getenv('DB_NAME', 'user_profile_db')

    SQLALCHEMY_DATABASE_URI = f'postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'
