import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'fastbites-dev-secret-key'
    UPLOAD_FOLDER = os.path.join('static', 'uploads')
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16MB max upload size
