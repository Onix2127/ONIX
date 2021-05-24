import json

from flask import Blueprint, url_for, request, render_template, jsonify
from pybo.models import Answer, Question, Userinfo, Mrvote
from datetime import datetime
import datetime as dt
from pybo import db
from pybo.weatherapi import get_wdata
from pybo.views.naverapi import navershop
from pybo.views.movieapi import Mrank, navermovie
from werkzeug.utils import redirect


bp = Blueprint('main', __name__, url_prefix='/')

@bp.route('/test')
def test():
    votenamelist = ['이찬원', '임영웅', '영탁', '정동원', '김호중', '김희재', '장민호']

    for i in votenamelist:
        vote = Mrvote(name=i, count=0)
        db.session.add(vote)

    db.session.commit()

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


@bp.route('/webhook', methods=('GET','POST'))
def webhook():
    # print('웹훅')
    req = request.get_json()
    # print(req)

    if req['queryResult']['intent']['displayName'] == 'movie ranking':
        rankdata = Mrank()
        result = ''
        count = 1
        for i in rankdata:
            result = result + str(count) + '위 :' + i['title']
            if count==3:
                break
            count += 1
        # print(rankdata)


    elif req['queryResult']['intent']['displayName'] == 'movie info_name':
        movieinfo = navermovie(req['queryResult']['queryText'])
        # print(movieinfo)
        moviedata = movieinfo['items'][0]

        return movie_info_img(moviedata['image'], moviedata['title'], moviedata['link'],
                              '감독:' + moviedata['director'] + ' 출연자' + moviedata['actor'])


    elif req['queryResult']['intent']['displayName'] == 'weather_que_city':
        winfo = get_wdata(req['queryResult']['queryText'])
        # print(winfo)
        return weather_info(winfo)


    # elif req['queryResult']['intent']['displayName'] == 'product_search_name':  #내가 짠 코드(하나만 보여짐)
    #     product = navershop(req['queryResult']['queryText'])
    #     # print(product)
    #     prodata = product['items'][0]
    #     # print(prodata)
    #
    #     return pro_info_img(prodata['image'], prodata['title'], prodata['link'],
    #                         '메이커: ' + prodata['maker'] + ' / 브랜드: ' + prodata['brand'] + ' / 최저가 : ' + prodata['lprice'] + '원')
    #
    elif req['queryResult']['intent']['displayName'] == 'product_search_name':  # 결과물 여러개 나오게 하기
        product = navershop(req['queryResult']['queryText'])
        return shop_infos(product['items'])


@bp.route('/mrvote', methods=('GET','POST'))
def mrvote():
    req = request.get_json()
    votename = req['queryResult']['queryText']
    votenamelist = ['이찬원', '임영웅', '영탁', '정동원', '김호중', '김희재', '장민호']

    if votename in votenamelist:
        voteresult = Mrvote.query.get_or_404(votename)
        print(voteresult.count)
        voteresult.count += 1
        db.session.commit()

        strdata = votename + "님에게 투표하셨습니다. 이용해주셔서 감사합니다."
        response_json = jsonify(
            fulfillment_text=strdata
        )
        print('===========투표시작===========')
        return response_json

    elif req['queryResult']['intent']['displayName'] == 'mrTrot_rank':
        vrankCnt = Mrvote.query.order_by(Mrvote.count.desc())

        result = ''
        count = 0
        for i in vrankCnt:
            count += 1
            result = result + str(count) + '위 :' + i.name + "  |  "

        response_json = jsonify(
            fulfillment_text=result
        )

    return response_json



def movie_info_img(imgurl, title, link, subtitle):
    response_json = jsonify(
        fulfillment_text='영화정보',
        fulfillment_messages=[
            {
                "payload": {
                    "richContent": [[
                        {
                            "type": "image",
                            "rawUrl": imgurl
                        },
                        {
                            "type": "info",
                            "title": title,
                            "actionLink": link,
                            "subtitle": subtitle
                        }
                    ]]
                }
            }
        ]
    )
    print(response_json)
    return response_json

def weather_info(winfo):
    strdata = ''

    if '지역' in winfo:
        strdata += winfo['지역'] + '의 '
    if '현재일기' in winfo and len(winfo['현재일기'])>1:
        strdata += '현재일기는 ' + winfo['현재일기'] + '이며, '
    if '현재기온' in winfo and len(winfo['현재기온'])>1:
        strdata += '현재기온은 ' + winfo['현재기온'] + '도, '
    if '일강수' in winfo and len(winfo['일강수'])>1:
        strdata += '일강수는 ' + winfo['일강수'] + 'mm'
    strdata += '입니다.'

    response_json = jsonify(
        fulfillment_text=strdata
    )
    return response_json

def pro_info_img(image, title, link, lprice):
    response_json = jsonify(
        fulfillment_text='제품정보',
        fulfillment_messages=[
            {
                "payload": {
                    "richContent": [[
                        {
                            "type": "image",
                            "rawUrl": image
                        },
                        {
                            "type": "info",
                            "title": title.replace("<b>","").replace("</b>",""),
                            "actionLink": link,
                            "subtitle": lprice
                        }
                    ]]
                }
            }
        ]
    )
    # print(response_json)
    return response_json

def shop_infos(items):

    plist = []
    for temp in items:
        imgurl = temp['image']
        title = temp['title']
        link = temp['link']
        subtitle = '최저가 :' + temp['lprice']
        listdata = [
            {
                "type": "image",
                "rawUrl": imgurl
            },
            {
                "type": "info",
                "title": title,
                "actionLink": link,
                "subtitle": subtitle
            }
        ]

        plist.append(listdata)

    response_json = jsonify(
        fulfillment_text=title,
        fulfillment_messages=[
            {
                "payload": {
                    "richContent": plist
                }
            }
        ]
    )

    return response_json