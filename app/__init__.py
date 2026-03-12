from flask import Flask
import os
import pymysql.cursors
from dotenv import load_dotenv

def create_app():
    app = Flask(__name__, template_folder='../templates', static_folder='../static')
    load_dotenv()

    app.config['MAX_CONTENT_LENGTH'] = 100 * 1024 * 1024
    app.secret_key = os.getenv('FLASK_SECRET_KEY', 'default_key')

    # Blueprint 등록 (앞으로 만들 파일들)
    from .news.routes import news_bp
    from .api.routes import api_bp
    from .board.routes import board_bp  # 게시판 추가

    app.register_blueprint(news_bp)
    app.register_blueprint(api_bp, url_prefix='/api')
    app.register_blueprint(board_bp, url_prefix='/board')

    return app

# DB 설정 (여러 Blueprint에서 공통으로 사용)
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
