# app/config/config.py

class Config:
    MONGO_URL_DEV = 'mongodb://localhost:27017/templates'
    MONGO_URL_PROD = 'mongodb+srv://kelinizkz:FFahOhTBTGeTRibT@kelinizkz.6md65.mongodb.net/templates'
    DEBUG = True
    FLASK_ENV = 'development'  # or 'production'

config = Config()