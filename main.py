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

# 查找所有ID为"video-title"的元素，并获取它们的href属性值
video_title_elements = soup.find_all(id='video-title')
for video_title_element in video_title_elements:
    # 获取href属性的值
    href_value = video_title_element.parent['href']  # Assuming the parent element contains the href attribute
    print(f"Text: {video_title_element.text}, href: {href_value}")