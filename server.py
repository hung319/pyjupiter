import os

# Thay đổi thư mục làm việc hiện tại thành thư mục chứa tệp này
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Chạy JupyterLab
os.system('jupyter lab')
