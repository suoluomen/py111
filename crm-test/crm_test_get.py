#encoding:UTF-8
'''
    通过get请求获取数据信息
'''
import json
import urllib.request
# from urllib import request
from urllib.parse import urlencode

data={}
ids=list(range(100))
data['isAjax']='1'

url_parame=urlencode(data).encode()

# all_url=url+url_parame
# all_url="http://www.baidu.com"
User_Agent=r'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'
Cookie=r'JSESSIONID=271u9c5wam1xds05v8fhhud4;'
headers = {'Cookie':Cookie,
           'User-Agent': User_Agent}
for id in ids:
    url = "http:// /os/cbm/contracts/"+str(id)
    request =urllib.request.Request(url,url_parame,headers,None,False,"GET")
    response = urllib.request.urlopen(request)

    result = response.read()
    record=result.decode('UTF-8')
    data=str(record)
    if data.__contains__("没有该条数据的权限")==False:
        dataJson=json.loads(data)
        print(dataJson['data'])


