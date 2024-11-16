from flask import Flask
from app.mongo import mongo
from app.routes import api
def create_app():
    app = Flask(__name__)
    app.config["MONGO_URI"] = "mongodb://mongo:27017/ashudb"
    app.register_blueprint(api)
    mongo.init_app(app)
    return app
