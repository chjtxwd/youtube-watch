import requests
import json
from bs4 import BeautifulSoup

url = 'https://flaresolverr.haijin666.top/v1'
headers = {
    'Content-Type': 'application/json'
}

data = {
    "cmd": "request.get",
    "url": "https://www.youtube.com/@cncf/videos",
    "maxTimeout": 60000
}

response = requests.post(url, headers=headers, json=data)

response = response.text
response = json.loads(response)
html = response['solution']['response']
soup = BeautifulSoup(html, 'html.parser')

# 创建一个空的列表，用于存储视频信息
videos = []

# 查找所有ID为"video-title"的元素，并获取它们的href属性值
video_title_elements = soup.find_all(id='video-title')
for video_title_element in video_title_elements:
    # 获取文本和href属性的值
    text = video_title_element.text
    href_value = video_title_element.parent['href']  # Assuming the parent element contains the href attribute
    # 将信息封装成JSON对象
    video_info = {"text": text, "href": href_value}
    # 添加到列表中
    videos.append(video_info)

# 将视频信息写入videos.json文件
with open('videos.json', 'w', encoding='utf-8') as json_file:
    json.dump(videos, json_file, ensure_ascii=False, indent=4)

print("Videos information has been written to videos.json")
