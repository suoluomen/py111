#encoding:UTF-8
'''
    通过put请求上传信息
'''
import json
import urllib.request
import requests

User_Agent=r'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'
Cookie=r'JSESSIONID=271u9c5wam1xds05v8fhhud4;'

id=43
url="http:// /os/cbm/contracts/effective/"+str(id)
postdata = { 'isAjax':'1' }

# r = requests.post(url,data=postdata)
#
# print(r.text)

# 如果要爬虫用的话 一般建议带上session会话和headers表头信息,session会话可以自动记录cookie

s = requests.Session()
headers = { 'Host':' ','Cookie':Cookie,
           'User-Agent': User_Agent,'Content-Type':'application/json'}
s.headers.update(headers)
i=1
while i>0:
    r=s.put(url, data="{'isAjax':'1'}")
    i=i-1
    print(r.text)
# r = s.put(url,data="{'isAjax':'1'}")
# print(r.text)


