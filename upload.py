from biliup.plugins.bili_webup import BiliBili, Data

def get_mp4_files(folder_path):
    mp4_files = []

    # 遍历目录
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            # 检查文件扩展名是否为 .mp4
            if file.endswith('.mp4'):
                # 构建完整的文件路径并添加到列表中
                file_path = os.path.join(root, file)
                mp4_files.append(file_path)

    return mp4_files


folder_path = '/r2'

# 遍历目录
for filename in os.listdir(folder_path):
    file_path = os.path.join(folder_path, filename)

    # 获取文件名（不包含路径）
    title = os.path.splitext(filename)[0]

    # 截取标题，使其不超过80个字符
    truncated_title = title[:80]

    # 构建新的文件名
    new_filename = truncated_title + '.mp4'

    # 构建新的文件路径
    new_file_path = os.path.join(folder_path, new_filename)

    # 重命名文件
    os.rename(file_path, new_file_path)



video = Data()
video.title = 'test'
video.desc = 'test'
video.source = '转载测试'
# 设置视频分区,默认为160 生活分区
video.tid = 231
video.set_tag(['CNCF', 'Youtube'])
with BiliBili(video) as bili:
    bili.login_by_password("username", "password")
    file_list =
    for file in file_list:
        video_part = bili.upload_file(file)  # 上传视频
    ret = bili.submit()  # 提交视频
