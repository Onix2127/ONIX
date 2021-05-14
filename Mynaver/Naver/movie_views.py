from flask import Blueprint

bp = Blueprint('Naver', __name__, url_prefix='/naver')

@bp.route('/movie')
def hello_Naver():
    return '네이버 영화정보 입니다.'