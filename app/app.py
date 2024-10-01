from flask import Flask
from flask_pymongo import PyMongo

from app.config.config import config

mongo = PyMongo()

def create_app():
    app = Flask(__name__)
    app.config['MONGO_URI'] = config.MONGO_URL
    app.config['DEBUG'] = config.DEBUG
    mongo.init_app(app)

    from app.routes.invite_routes import invite_bp
    app.register_blueprint(invite_bp)

    return app