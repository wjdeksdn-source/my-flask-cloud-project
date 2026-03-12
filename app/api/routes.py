from flask import Blueprint

api_bp = Blueprint('api', __name__)

@api_bp.route('/')
def api_index():
    return {"status": "success", "message": "API System Online"}
