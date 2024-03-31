import logging
import os
import shutil
import tkinter as tk
import tkinter.messagebox as msgbox
import win32api
import datetime

# 检查并创建日志文件
log_file_path = "D:\getfromusb\lastlog.txt"
os.makedirs(os.path.dirname(log_file_path), exist_ok=True)
if not os.path.exists(log_file_path):
    open(log_file_path, 'w').close()

logging.basicConfig(filename=log_file_path, level=logging.DEBUG, format="[%(asctime)s] %(message)s")

def submit():
    global qudong
    global recent_files_count
    qudong = str(entry_drive.get())
    recent_files_count = int(entry_count.get())
    window.destroy()

# 创建窗口
window = tk.Tk()
window.title("确认盘符和文件数量")

# 创建标签和文本框（盘符）
label_drive = tk.Label(window, text="请输入要读取的盘符：")
label_drive.pack()
entry_drive = tk.Entry(window)
entry_drive.pack()

# 创建标签和文本框（文件数量）
label_count = tk.Label(window, text="请输入要获取的最近文件的数量：")
label_count.pack()
entry_count = tk.Entry(window)
entry_count.pack()

# 创建按钮
button = tk.Button(window, text="确定并运行", command=submit)
button.pack()

# 运行窗口
window.mainloop()

while True:
    try:
        drives = win32api.GetLogicalDriveStrings()
        drives = drives.split('\000')[:-1]
        for drive in drives:
            if qudong in drive:
                print('U盘已插入')
                logging.info('U盘已插入')
                break
        else:
            continue
        break
    except Exception as e:
        print(f"获取驱动器出错: {e}")
        logging.error(f"获取驱动器出错: {e}")
        break

# 源文件夹路径和目标文件夹路径
source_folder = qudong + ':\\'  # U盘的盘符
dest_folder = 'D:\\getfromusb\\'  # 目标文件夹路径

# 创建文件夹
try:
    if not os.path.exists(dest_folder):
        os.makedirs(dest_folder)
except Exception as e:
    print(f"创建目标文件夹失败: {e}")
    logging.error(f"创建目标文件夹失败: {e}")
    exit()

# 遍历文件
ppt_files = []
for root, dirs, files in os.walk(source_folder):
    for file in files:
        if file.endswith('.ppt') or file.endswith('.pptx'):
            source_file_path = os.path.join(root, file)
            ppt_files.append((source_file_path, os.path.getmtime(source_file_path)))

# 获取最近的文件
if len(ppt_files) > 0:
    ppt_files.sort(key=lambda x: x[1], reverse=True)
    ppt_files = ppt_files[:recent_files_count]

# 复制文件
for file_info in ppt_files:
    file, _ = file_info
    dest_file_path = os.path.join(dest_folder, os.path.basename(file))
    try:
        shutil.copy2(file, dest_file_path)
        print(f"成功将文件 {file} 复制到 {dest_file_path}")
        logging.info(f"成功将文件 {file} 复制到 {dest_file_path}")
    except Exception as e:
        print(f"复制文件 {file} 失败: {e}")
        logging.error(f"复制文件 {file} 失败: {e}")
