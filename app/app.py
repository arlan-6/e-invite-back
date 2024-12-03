
from flask import Flask
from flask_pymongo import PyMongo
from app.config.config import config
from flask_cors import CORS
mongo = PyMongo()

def create_app():
    app = Flask(__name__)

    # app.config['MONGO_URI'] = config.MONGO_URL
    # app.config['DEBUG'] = config.DEBUG
    # mongo.init_app(app)


    if config.FLASK_ENV == 'production':
        app.config['MONGO_URI'] = config.MONGO_URL_PROD
    else:
        app.config['MONGO_URI'] = config.MONGO_URL_DEV

    app.config['DEBUG'] = config.DEBUG
    mongo.init_app(app)

    CORS(app, resources={r"/*": {"origins": ["http://localhost:3000", "https://keliniz-kz.vercel.app"]}})

    from app.routes.invite_routes import invite_bp
    app.register_blueprint(invite_bp)


    return app