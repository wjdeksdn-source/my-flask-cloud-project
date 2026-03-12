from flask import Blueprint, render_template

news_bp = Blueprint('news', __name__)

@news_bp.route('/')
def news_list():
    return {"status": "success", "message": "News list loaded (v1.1)"}
