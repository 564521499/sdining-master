import json
import re
import requests
from lxml import etree


def getVideo(url):
    # 请求要下载的url地址
    html = requests.get(url)
    # 转化为页面文本
    jsonRes = html.text
    # 匹配:wxv_1105179750743556096
    dirRe = r"wxv_.{19}"
    # 页面文本里通过正则搜索匹配
    result = re.search(dirRe, jsonRes)
    # 结果判断
    if result:
        wxv = result.group(0)
        print(wxv)
        # 页面播放形式
        # video_url = "https://mp.weixin.qq.com/mp/readtemplate?t=pages/video_player_tmpl&auto=0&vid=" + wxv
        # print("video_url", video_url)
        # 页面可下载形式 固定的url
        video_url_temp = "https://mp.weixin.qq.com/mp/videoplayer?action=get_mp_video_play_url&preview=0&__biz=MzU1MTg5NTQxNA==&mid=2247485507&idx=4&vid=" + wxv
        content = json.loads(requests.get(video_url_temp).content.decode())
        print('content:', content)

        url_info = content.get("url_info")

        # 获取文章封面图片
        mator_img = etree.HTML(jsonRes).xpath("//meta[@property='og:image']/@content")
        print('mator_img', mator_img)

        if url_info:
            video_url2 = url_info[0].get("url")
            print('vedio_url:', video_url2)
            return video_url2
        else:
            return ""

    else:
        return ""


if __name__ == '__main__':
    # 公众号链接地址
    url_all = 'https://mp.weixin.qq.com/s/EzYQS3hKvPmQhSnAjEFbIw'
    getVideo(url_all)
