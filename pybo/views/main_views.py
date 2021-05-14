from flask import Blueprint, url_for, request, render_template
from pybo.models import Answer, Question, Userinfo
from datetime import datetime
import datetime as dt
from pybo import db
from werkzeug.utils import redirect


bp = Blueprint('main', __name__, url_prefix='/')

@bp.route('/test')
def test():
    # for i in range(100):
    #     q = Question(subject='테스트 데이터 [%03d]'%i, content='내용무', create_date=datetime.now())
    #     db.session.add(q)
    # db.session.commit()
    return redirect(url_for('main.index'))

# --------------------------------- [edit] ---------------------------------- #
@bp.route('/hello')
def hello_pybo():

    # for i in range(10):
    #     i = Question(subject='flask를 통해 무엇을 얻을 수 있나요? ', content='flask의 기능에 대해 알고싶습니다.', create_date=datetime.now())
    #     db.session.add(i)
    # db.session.commit()

    return 'Hello, Pybo!'


@bp.route('/')
def index():
    return redirect( url_for('question._list'))
# --------------------------------------------------------------------------- #

@bp.route('/detail/<int:question_id>/')
def detail(question_id):
    question = Question.query.get_or_404(question_id)
    return render_template('question/question_detail.html', question=question)