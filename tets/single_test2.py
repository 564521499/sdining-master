from copy import deepcopy

from lxml import etree

from tets.single_test import Singleton, Mets
# a = Singleton()
# b = Singleton()
# c = Mets()
# d = Mets()
# e = Singleton()
#
# print('a--',a,'b--',b,)
# print('c--',c,'d--',d,'e--',e)
#
# str1 = ['sdfds','sdewr','wewefd']
# hehe = str1
# haha = deepcopy(str1)
# hehe.append('hgscdysfdcsdcsd')
# haha.append('jhsdfyufs')
# print(hehe)
# print(haha)
#
# import requests
#
# session = requests.session()
# data = {
#     "loginName": 15019735233,
#     "password": "xmm1234567899"
# }
#
# url = "https://passport.17k.com/ck/user/login"
# a = session.post(url, data=data)
#
# print('cookies',a.cookies)
# resp = session.get("https://user.17k.com/ck/author/shelf?page=1&appKey=2406394919")
#
# print('回取数据',resp.json())
#
# resp = requests.get("https://user.17k.com/ck/author/shelf?page=1&appKey=2406394919",
#                     headers={
#                         "Cookie": "GUID=f9fff4a8-3101-4b8a-b29a-b1cb2beaacb3; sajssdk_2015_cross_new_user=1; Hm_lvt_9793f42b498361373512340937deb2a0=1655801330; c_channel=0; c_csc=web; BAIDU_SSP_lcr=https://graph.qq.com/oauth2.0/show?which=Login&display=pc&response_type=code&client_id=215314&scope=get_user_info&redirect_uri=https%3A%2F%2Fpassport.17k.com%2Fsns%2FqqCallback.action%3FfromUrl%3Dhttps%253A%252F%252Fwww.17k.com%252F; accessToken=avatarUrl%3Dhttps%253A%252F%252Fcdn.static.17k.com%252Fuser%252Favatar%252F07%252F67%252F44%252F97104467.jpg-88x88%253Fv%253D1655801509000%26id%3D97104467%26nickname%3Dpythonnnn%26e%3D1671353540%26s%3D59e44ffcfb6925c4; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2297104467%22%2C%22%24device_id%22%3A%2218185733a0a372-01989555b8fb9a-50684254-921600-18185733a0c6df%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E5%BC%95%E8%8D%90%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22https%3A%2F%2Fgraph.qq.com%2Foauth2.0%2Fshow%3Fwhich%3DLogin%26display%3Dpc%26response_type%3Dcode%26client_id%3D215314%26scope%3Dget_user_info%26redirect_uri%3Dhttps%253A%252F%252Fpassport.17k.com%252Fsns%252FqqCallback.action%253FfromUrl%253Dhttp%22%2C%22%24latest_referrer_host%22%3A%22graph.qq.com%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC%22%7D%2C%22first_id%22%3A%22f9fff4a8-3101-4b8a-b29a-b1cb2beaacb3%22%7D; Hm_lpvt_9793f42b498361373512340937deb2a0=1655801671"})


# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
#
#
# class Solution:
#     def ReverseList(self, head: ListNode) -> ListNode:
#         # write code here
#         pre = None
#         head = head
#         while head:
#             # temp为第一个值
#             first = head.next
#             # 拿到做后一个head
#             head.next = pre
#             pre = head
#             print(pre)
#             # 最后一个值head赋值变更为第一个值
#             head = first
#
#         return pre
#
# Solution.ReverseList({1,2,3})
#
# a = 6
# b = 8

# list1 = [1,2,3,4,5]
# # list1.pop()
# print(list1)
import requests
#
url = "https://mp.weixin.qq.com/s/vU_I_4YwDP8d99pmA7XleQ"
headers = {"User-Agent": "Mozilla/5.0"}

response = requests.get(url=url,headers=headers).text

r=etree.HTML(response)

result  = r.xpath("//*[@id='js_mpvedio_1667552447995_964793605089']/div/div[17]/div[1]/video")
# for i in result:
#     print(i.text)
print(result)
# word = 'bfkc'
#
# matrix = [['a', 'b', 'c', 'd'],
#           ['b', 'f', 'k', 'y'],
#           ['n', 'm', 'c', 'z']]
# left = 0
# right = 0
# up = 0
# dn = 0
# dict_zuo = {}
# word_l = word.split('')
# n = 0
# while len(word_l)>0:
#     for m in matrix:
#         if word_l[n] in m:
#             x, y = matrix.index(m), m.index(word_l[n])
#             if word_l[n+1] == matrix[x+1][y]:
#
#
#             if
#
# print(dict_zuo)
