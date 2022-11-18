

import requests
import re
from lxml import etree

# url_all = 'https://mp.weixin.qq.com/s/vU_I_4YwDP8d99pmA7XleQ'
# url_all = 'https://mp.weixin.qq.com/s/YVvccg-I8DAYZ4t9S4sGFQ'
url_all = 'https://mp.weixin.qq.com/s/3g4gDpZHq0H9AHPnHNC0uw'
headers = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'}
html = requests.get(url_all,headers=headers).content.decode('utf-8')
print(html)


##################################
pattern = re.compile(r"http://mpvideo.qpic.cn/[^\s]*[',]")
vedio_url = re.findall(pattern, html)
print(vedio_url)
for i in vedio_url:
    print('视频：', i.replace(r'\x26amp;', '&').replace("',", ''))

pattern_vid = re.compile(r"wxv_[^\s]*[',]")
vid_url = re.findall(pattern_vid, html)
print('vid:',vid_url)
#################################################################3

# 匹配 标题视频封面图
mator_img = etree.HTML(html).xpath("//meta[@property='og:image']/@content")
print('mator_img', mator_img)


"""
<video data-v-5d169733="" 
src="http://mpvideo.qpic.cn/0bc3paagwaaakeagvmtgmrrva6gdnn4aa2ya.f10002.mp4?dis_k=8f63e16970b5b73c4c3c505470c40319&amp;dis_t=1667802324&amp;
vid=wxv_2651422268979429377&amp;
format_id=10002&amp;support_redirect=0&amp;mmversion=false" 
poster="http://mmbiz.qpic.cn/mmbiz_jpg/Cb2oh8G1Oen45mpiaEETib6A1scY8Kf7B2ah786tKSWOquYzv6bT7rnaoZt4gBpeVjgV9gmpniaZUpDzRoVoWiaOkg/0?wx_fmt=jpeg" 
webkit-playsinline="isiPhoneShowPlaysinline" playsinline="isiPhoneShowPlaysinline" preload="metadata" crossorigin="anonymous" controlslist="nodownload" 
class=""> 您的浏览器不支持 video 标签 </video>
"""