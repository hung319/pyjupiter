import os
from jupyter_server.serverapp import ServerApp

# Đặt mật khẩu
os.environ['JUPYTER_LAB_PASSWORD'] = os.getenv('PASSWORD', 'your_default_password')

# Khởi động JupyterLab
server = ServerApp()
server.launch_instance()
