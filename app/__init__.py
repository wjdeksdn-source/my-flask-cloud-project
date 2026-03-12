from flask import Flask
import os
import pymysql.cursors
from dotenv import load_dotenv

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

def create_app():
    # 현재 디렉토리 구조에 맞춰 템플릿과 스테틱 경로 설정
    app = Flask(__name__, template_folder='../templates', static_folder='../static')
    load_dotenv()

    app.config['MAX_CONTENT_LENGTH'] = 100 * 1024 * 1024
    app.secret_key = os.getenv('FLASK_SECRET_KEY', 'default_key')

    # 메인 페이지 라우트 (v1.1 확인용)
    @app.route('/')
    def index():
        return "Hello, DevOps World! (v1.1) - Main Page"

    # Blueprint 불러오기 및 등록
    from .news.routes import news_bp
    from .api.routes import api_bp
    from .board.routes import board_bp

    # 각 서비스별 경로(prefix) 설정
    app.register_blueprint(news_bp, url_prefix='/news')
    app.register_blueprint(api_bp, url_prefix='/api')
    app.register_blueprint(board_bp, url_prefix='/board')

    return app
