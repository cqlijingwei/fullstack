from flask import Flask
from routers import index
from flask_cors import CORS


def create_app():
    app = Flask(__name__)
    CORS(app, resources={r"/*": {"origins": "*"}})
    app.register_blueprint(index)
    return app
