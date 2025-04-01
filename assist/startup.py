import os
import shutil

def startup_main(exe_path):
    startup_folder = os.path.join(os.getenv('APPDATA'), 'Microsoft', 'Windows', 'Start Menu', 'Programs', 'Startup')
    if not os.path.exists(startup_folder):
        os.makedirs(startup_folder)
    exe_name = os.path.basename(exe_path)
    destination_path = os.path.join(startup_folder, exe_name)
    shutil.copy(exe_path, destination_path)
    print(f"文件已复制到启动文件夹: {destination_path}")