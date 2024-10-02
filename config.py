import os

# Configuration settings
class Config:
    DEBUG = True
    DATABASE_URL = os.getenv('DATABASE_URL', 'sqlite:///cityai.db')
    API_KEY = os.getenv('API_KEY', 'your_api_key_here')
