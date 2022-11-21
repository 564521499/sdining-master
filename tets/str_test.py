# allo = "ab"
# words = ["ad","bd","aaab","baa","badab"]
#
# a = []
# for i in words:
#     a.append(all([x in set(allo) for x in i]))
# print(a)
#
# for m in range(3,5):
#     print(m)

# import tesserocr
# from PIL import Image
#
# image = r'G:\自测\sdining-master\12.jpg'
# open_img = Image.open(image)
# result = tesserocr.im
import json

import requests

url = 'http://42.193.70.162:443/api/templates/findSqlReportList'
headers = {
'Cokkie':'YJPINFO=2dd1e95a-415d-4c9a-9794-24264512c6ab; YJPID=984eb368a71b4ad78ed35fcb919bf067',
'Accept': 'application/json',
'Content-Type':'application/json',
'Host': 'scop1.yijiupi.com',
'Origin': 'https://scop1.yijiupi.com',
'Referer': 'https://scop1.yijiupi.com/',
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36',
'x-sign': '7c1e34f25ae008e2bb6844abb1058bfb6e08057a',
'x-sign-nonce': '2217ac36_5c2c_4550_8b31_79cb814d58e2',
'x-sign-timestamp':'1668849254',
'x-sign-version': '1.0',
}
parmas = {"taskName":"","pageSize":10,"pageNum":1}
a = requests.post(url,data=json.dumps(parmas)).text
print(a)