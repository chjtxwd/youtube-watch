import requests
import json
import sqlite3
from bs4 import BeautifulSoup
from datetime import datetime

def get_html_text(url):
    flaresolverr = 'https://flaresolverr.haijin666.top/v1'
    headers = {
    'Content-Type': 'application/json'
     }

    data = {
    "cmd": "request.get",
    "url": url,
    "maxTimeout": 60000
    }

    response = requests.post(flaresolverr, headers=headers, json=data)
    response_text = response.text
    return response_text


def create_table(cursor):
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS videos (
            id INTEGER PRIMARY KEY,
            title TEXT,
            description TEXT,
            url TEXT,
            longtitle TEXT,
            longdescription TEXT,
            created_at TIMESTAMP,
            uploaded_at TIMESTAMP
        )
    ''')

def video_exists(cursor, url):
    cursor.execute('''
        SELECT 1 FROM videos WHERE url = ?
    ''', (url,))
    return cursor.fetchone() is not None

def insert_video(cursor, video):
    cursor.execute('''
        INSERT INTO videos (title, description, url, created_at)
        VALUES (?, ?, ?, ?)
    ''', (video['text'], '', video['href'], datetime.now()))

def print_all_urls(cursor):
    cursor.execute('''
        SELECT url FROM videos
    ''')
    urls = cursor.fetchall()
    for url in urls:
        url =   +url


url = "https://www.youtube.com/@cncf/videos"
response = get_html_text(url)
response = json.loads(response)
html = response['solution']['response']
soup = BeautifulSoup(html, 'html.parser')

# 连接到 SQLite 数据库
# 数据库不存在时会被自动创建
conn = sqlite3.connect('my_database.db')
c = conn.cursor()

# 创建表
create_table(c)

# 查找所有ID为"video-title"的元素，并获取它们的href属性值
video_title_elements = soup.find_all(id='video-title')
for video_title_element in video_title_elements:
    # 获取文本和href属性的值
    text = video_title_element.text
    href_value = video_title_element.parent['href']  # Assuming the parent element contains the href attribute

    # 如果视频不存在于数据库中，则添加到数据库并打印出来
    if not video_exists(c, href_value):
        print(f'New video found: {text} ({href_value})')
        insert_video(c, {'text': text, 'href': href_value})

# 提交事务
conn.commit()

# 关闭连接
conn.close()


# 查找每一个 视频 url, 获得 long_description long_title

# 连接到 SQLite 数据库
conn = sqlite3.connect('my_database.db')
c = conn.cursor()

# 调用函数打印所有URL
print("All URLs in the database:")
print_all_urls(c)

# 关闭连接
conn.close()