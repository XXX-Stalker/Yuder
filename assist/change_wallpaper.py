import ctypes
import os

def change_wallpaper(image_path):
    if not os.path.exists(image_path):
        print("指定的图片路径不存在！")
        return
    ctypes.windll.user32.SystemParametersInfoW(20, 0, image_path, 3)  # 添加参数 3
    print("壁纸已成功更改！")

def change_wallpaper_main():
    # 获取当前脚本所在的文件夹路径
    current_folder = os.path.dirname(os.path.abspath(__file__))
    # 拼接图片的绝对路径
    image_path = os.path.join(current_folder, r"1.jpg")
    change_wallpaper(image_path)