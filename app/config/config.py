import os
from dotenv import load_dotenv

load_dotenv()

class Config():
    MONGO_URL = os.getenv("MONGO_URL")
    DEBUG = os.getenv("FLASK_ENV") == 'development'

config = Config()