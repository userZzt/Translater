# coding=utf-8
# Author:Tommy_Sea
# Time:2019-8
'''
URLLIB
url就是网页，一般的格式为：（带[] 的为可选项）
protocol://hostname[:port]/path/[;parameters][?query]#fragment

第一部分协议：http，https，ftp，file，ed2k...
第二部分：是存放资源的服务器的域名系统或IP地址（有时候包括端口号）
第三部分：是资源的具体地址，如目录或文件名

'''
import urllib.request as urlr
import urllib.parse as urlp
import json
#############Get Cat
# response = urlr.urlopen('http://placekitten.com/g/500/600')
# cat_img = response.read()
#
# with open('cat_500_600.jpg','wb') as f:#使用with不用手动关闭文件
#     f.write(cat_img)


########Translation

url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'
# head = {}
# head['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'

data={}
data['i']=str(input("Please input your words here：\n"))
data['from']= 'AUTO'
data['to']= 'AUTO'
data['smartresult']= 'dict'
data['client']= 'fanyideskweb'
data['salt']= '15667857579663'
data['sign']='fbb454d6b39370b3c40327a23dff07ed'
data['ts']='1566785757966'
data['bv']='94d71a52069585850d26a662e1bcef22'
data['doctype']='json'
data['version']= '2.1'
data['keyfrom']= 'fanyi.web'
data['action']= 'FY_BY_CLICKBUTTION'

data = urlp.urlencode(data).encode('utf-8')
# req = urlr.Request(url,data,head)
req = urlr.Request(url,data)
req.add_header('User-Agent','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36')
response = urlr.urlopen(req)
html = response.read().decode('utf-8')
target=json.loads(html)#解为字典形式
#print(target)
print("'{0}'------->'{1}'".format(target['translateResult'][0][0]['src'],target['translateResult'][0][0]['tgt']))
