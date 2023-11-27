import sqlite3
import subprocess

def get_videos_without_upload_time(cursor):
    cursor.execute('''
        SELECT title, url FROM videos WHERE uploaded_at IS NULL
    ''')
    return cursor.fetchall()

# 连接到 SQLite 数据库
conn = sqlite3.connect('my_database.db')
c = conn.cursor()

# 获取没有上传时间的视频
videos = get_videos_without_upload_time(c)

for video in videos:
    title, url = video
    full_url = 'https://www.youtube.com/' + url
    print(f'Downloading video: {title} ({full_url})')

    # 调用 yt-dlp 来下载视频
    subprocess.run(['/root/yt-dlp_linux', full_url , '-P /r2/'])

    # 更新视频的上传时间
    c.execute('''
        UPDATE videos SET uploaded_at = CURRENT_TIMESTAMP WHERE url = ?
    ''', (url,))

# 提交事务
conn.commit()

# 关闭连接
conn.close()
