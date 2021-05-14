import json
import os
import sys
import urllib.request
from bs4 import BeautifulSoup
import requests
import lxml

def Mrank():
    page = requests.get('https://movie.naver.com/movie/running/current.nhn')
    html = page.text
    #print(html)
    soup = BeautifulSoup(html,'lxml')
    result = soup.find_all('dl','lst_dsc') # dl의 lst_dsc에 해당하는 데이터 가져옴

    moviedata = []

    for temp in result:
        mdata = {}

        # 제목
        tdata = temp.find('dt','tit')
        tdata = tdata.find('a').text
        mdata['title'] = tdata
        #print(mdata)

        # 평점
        sdata = temp.find('div','star_t1')
        sdata = sdata.find('span','num').text
        mdata['star'] = sdata
        # print(sdata)
        # print(mdata)

        # 장르
        genre = temp.find('dl','info_txt1')
        genre = genre.find('span', 'link_txt').text.replace('\n','').replace('\r','').replace('\t','')
        mdata['genre'] = genre
        # print(mdata)

        moviedata.append(mdata)


    # -------------------# 썸네일 이미지 데이터 # -------------------#
    imgresult = soup.find_all('div','thumb')
    imgurl = []
    for temp in imgresult:
        url = temp.find('img')
        imgurl.append(url['src'])
        # print(url['src'])

    # print(imgurl)

    # print(imgresult)

    i=0
    for temp in moviedata:
        temp['img'] = imgurl[i]
        i+=1
        print(temp)

    # print(moviedata)

    return moviedata


# response = requests.get(url)

# print(response.status_code)
# print(response.text)

# if response.status_code == 200:
#     html = response.text
#     soup = BeautifulSoup(html, 'html.parser')
#     ol = soup.select_one('#contents > div.wrap-movie-chart > div.sect-movie-chart')
#     title = ol.find_all('strong')
#     # print(soup)
#
# else :
#     print(response.status_code)
#
# # print(title.get_text())
# print(title)


def navermovie(moviename):
    client_id = "HC3S55ERnghyGn1dPN4q"
    client_secret = "KT4_YPZwmi"
    encText = urllib.parse.quote(moviename)
    url = "https://openapi.naver.com/v1/search/movie?query=" + encText # json 결과
    # url = "https://openapi.naver.com/v1/search/blog.xml?query=" + encText # xml 결과
    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id",client_id)
    request.add_header("X-Naver-Client-Secret",client_secret)
    response = urllib.request.urlopen(request)
    rescode = response.getcode()
    if(rescode==200):
        response_body = response.read()
        # print(response_body.decode('utf-8'))
        jsontemp = json.loads(response_body.decode('utf-8'))   #네이버에서 준 코드
        #
        # # print(jsontemp['items'])
        # # print(len(jsontemp['items']))
        #
        # for temp in jsontemp['items']:
        #     print(temp['title'])

    else:
        print("Error Code:" + rescode)

    return jsontemp