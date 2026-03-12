from flask import Blueprint

board_bp = Blueprint('board', __name__)

@board_bp.route('/')
def board_index():
    return {"status": "success", "message": "Board System Online"}
