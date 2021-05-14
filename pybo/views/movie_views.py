from datetime import datetime
from flask import Blueprint, render_template, request, url_for, flash, session, g
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import redirect
from pybo import db
from pybo.form import NaverMovieForm
from pybo.models import Question, User
from pybo.views.movieapi import Mrank, navermovie

bp = Blueprint('movierank', __name__, url_prefix='/movie')

@bp.route('/rank/')
def Movierank():
    rankdata = Mrank()
    # print(rankdata)

    return render_template('movie/movierank.html', rankdata=rankdata)

@bp.route('/msearch/', methods=('GET','POST'))
def Navermovie():
    form = NaverMovieForm()

    if request.method == "POST" and form.validate_on_submit():
        print(form.moviesearch.data)
        result = navermovie(form.moviesearch.data)

        return render_template('movie/navermovie.html', movieinfo_list=result['items'], form=form)

    return render_template('movie/navermovie.html', form=form)

# redirect(url_for('naver.book', question_id=question_id))
