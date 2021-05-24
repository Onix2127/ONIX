# -*- coding: utf-8 -*-
import json

result = {'lastBuildDate': 'Fri, 21 May 2021 10:38:11 +0900', 'total': 74721, 'start': 1, 'display': 10, 'items': [{'title': '삼성전자 <b>비스포크</b> RF85T91S1AP', 'link': 'https://search.shopping.naver.com/gate.nhn?id=24395126522', 'image': 'https://shopping-phinf.pstatic.net/main_2439512/24395126522.20201008161501.jpg', 'lprice': '1639000', 'hprice': '', 'mallName': '네이버', 'productId': '24395126522', 'productType': '1', 'brand': '비스포크', 'maker': '삼성전자', 'category1': '디지털/가전', 'category2': '주방가전', 'category3': '냉장고', 'category4': '양문형냉장고'}, {'title': '삼성전자 <b>비스포크</b> RF85T9111T2', 'link': 'https://search.shopping.naver.com/gate.nhn?id=22780234399', 'image': 'https://shopping-phinf.pstatic.net/main_2278023/22780234399.20200715121509.jpg', 'lprice': '1592450', 'hprice': '', 'mallName': '네이버', 'productId': '22780234399', 'productType': '1', 'brand': '비스포크', 'maker': '삼성전자', 'category1': '디지털/가전', 'category2': '주방가전', 'category3': '냉장고', 'category4': '양문형냉장고'}, {'title': '삼성전자 <b>비스포크</b> RF85T9111AP', 'link': 'https://search.shopping.naver.com/gate.nhn?id=22680051522', 'image': 'https://shopping-phinf.pstatic.net/main_2268005/22680051522.20200518171924.jpg', 'lprice': '1641950', 'hprice': '', 'mallName': '네이버', 'productId': '22680051522', 'productType': '1', 'brand': '비스포크', 'maker': '삼성전자', 'category1': '디지털/가전', 'category2': '주방가전', 'category3': '냉장고', 'category4': '양문형냉장고'}, {'title': '삼성전자 <b>비스포크</b> RB33T3004AP', 'link': 'https://search.shopping.naver.com/gate.nhn?id=23087372490', 'image': 'https://shopping-phinf.pstatic.net/main_2308737/23087372490.20200623122527.jpg', 'lprice': '638820', 'hprice': '', 'mallName': '네이버', 'productId': '23087372490', 'productType': '1', 'brand': '비스포크', 'maker': '삼성전자', 'category1': '디지털/가전', 'category2': '주방가전', 'category3': '냉장고', 'category4': '일반형냉장고'}, {'title': '삼성전자 <b>비스포크</b> RF60A91C3AP', 'link': 'https://search.shopping.naver.com/gate.nhn?id=26394480522', 'image': 'https://shopping-phinf.pstatic.net/main_2639448/26394480522.20210317165059.jpg', 'lprice': '1940000', 'hprice': '', 'mallName': '네이버', 'productId': '26394480522', 'productType': '1', 'brand': '비스포크', 'maker': '삼성전자', 'category1': '디지털/가전', 'category2': '주방가전', 'category3': '냉장고', 'category4': '양문형냉장고'}]}
jdata = json.dumps(result)
jdata = json.loads(jdata)

# 1. 결과값으로 받은 제품의 갯수를 파악
a = jdata['items']
# print(len(a))


# 2. 이름값 추출
titlelist = []
for temp in jdata['items']:
    titlelist.append(temp['title'])

# print(titlelist)

# 3. 이름, 가격, 몰이름
plist = []
for temp in jdata['items']:
    pdict = {}
    pdict['제품명'] = temp['title'].replace("<b>","").replace("</b>","")
    pdict['가격'] = temp['lprice']
    pdict['판매몰'] = temp['mallName']

    plist.append(pdict)

print(plist)