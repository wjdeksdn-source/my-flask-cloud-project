from flask import Flask
import os
import pymysql.cursors
from dotenv import load_dotenv

DB_CONFIG = {
    'host': os.getenv('DB_HOST', '192.168.0.13'),
    'user': os.getenv('DB_USER', 'flask_user'),
    'password': os.getenv('DB_PASSWORD', 'P@ssw0rd'),
    'db': os.getenv('DB_NAME', 'flask_auth_db'),
    'charset': 'utf8mb4',
    'cursorclass': pymysql.cursors.DictCursor
}

def get_db_connection():
    return pymysql.connect(**DB_CONFIG)

def create_app():
    app = Flask(__name__, template_folder='../templates', static_folder='../static')
    load_dotenv()
    app.config['MAX_CONTENT_LENGTH'] = 100 * 1024 * 1024
    app.secret_key = os.getenv('FLASK_SECRET_KEY', 'default_key')

    @app.route('/')
    def index():
        return "Hello, DevOps World! (v1.1) - Main Page"

    from .news.routes import news_bp
    from .api.routes import api_bp
    from .board.routes import board_bp

    app.register_blueprint(news_bp, url_prefix='/news')
    app.register_blueprint(api_bp, url_prefix='/api')
    app.register_blueprint(board_bp, url_prefix='/board')

    return app
