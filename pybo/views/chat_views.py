from datetime import datetime
from flask import Blueprint, render_template, request, url_for
from werkzeug.utils import redirect
from pybo import db
from pybo.form import QuestionForm, AnswerForm, HelpForm
from pybo.models import Question
from pybo.views.dialogflowapi import chat

bp = Blueprint('chat', __name__, url_prefix='/chat')


@bp.route('/bot/')
def Bot():
    return render_template('chat/chatbot.html')

@bp.route('/help/', methods=('GET','POST'))
def Help():
    form = HelpForm()
    if request.method == "POST" and form.validate_on_submit():
        result = chat(form.search.data,'1234')
        print(result)
        if result == '영화 순위 메뉴':
            return redirect(url_for('movierank.Movierank'))
        elif result == 'Go google':
            return redirect('http://www.google.com', code=302)


    return render_template('chat/help.html', form=form)

@bp.route('/chatvote/')
def chatVote():
    return render_template('chat/chatvote.html')