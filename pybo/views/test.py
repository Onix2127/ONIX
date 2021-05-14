import json
import os
import sys
import urllib.request



client_id = "HC3S55ERnghyGn1dPN4q"
client_secret = "KT4_YPZwmi"
encText = urllib.parse.quote('007')
url = "https://openapi.naver.com/v1/search/movie?query=" + encText # json 결과
#url = "https://openapi.naver.com/v1/search/movie.xml?query=" + encText # xml 결과
print(url)
request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)
response = urllib.request.urlopen(request)
print(response)
rescode = response.getcode()
print(rescode)