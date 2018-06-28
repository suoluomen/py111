# from urllib import request
import json

# def fetch_data(url):
#     with request.urlopen(url) as f:
#         return json.loads(f.read().decode('utf-8'))
# URL = 'https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woeid%20%3D%202151330&format=json'
# data = fetch_data(URL)
# print(data)
# assert data['query']['results']['channel']['location']['city'] == 'Beijing'
# print('ok')



# 获取页面信息
# -*- coding: UTF-8 -*-
from urllib import request
import chardet

if __name__ == "__main__":
    response = request.urlopen("https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woeid%20%3D%202151330&format=json")
    html = response.read()
    # charset = chardet.detect(html)
    # ut=charset['encoding']
    # # print(ut)
    html = html.decode('utf-8')
    data=json.loads(html)
    print(data['query'])
    # print(html)