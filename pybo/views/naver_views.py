from datetime import datetime
from flask import Blueprint, render_template, request, url_for, flash, session, g
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import redirect
from pybo import db
from pybo.form import NaverBookForm
from pybo.models import Question, User
from pybo.views.naverapi import naverbook

bp = Blueprint('naver', __name__, url_prefix='/naver')

@bp.route('/book/', methods=('GET','POST'))  # 책 페이지 접근
def Naverbook():
    form = NaverBookForm()

    if request.method == "POST" and form.validate_on_submit():
        print(form.search.data)
        result = naverbook(form.search.data)

        return render_template('naver/naverbook.html', bookinfo_list=result['items'], form=form)

    return render_template('naver/naverbook.html', form=form)

# redirect(url_for('naver.book', question_id=question_id))


