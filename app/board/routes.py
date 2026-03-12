from flask import Blueprint, render_template, request, session, flash, redirect, url_for
from app import get_db_connection  # 공통 DB 연결 사용

board_bp = Blueprint('board', __name__)

@board_bp.route('/')
def board_list():
    # 기존 board_list 함수 내용 복사
    if 'loggedin' not in session:
        return redirect(url_for('index'))
    # ... (생략) ...
    return render_template('board_list.html', posts=posts)

@board_bp.route('/write', methods=['GET', 'POST'])
def write_post():
    # 기존 write_post 함수 내용 복사
    # ... (생략) ...
    return render_template('write_post.html')
