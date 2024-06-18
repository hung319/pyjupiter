import os
from jupyter_server.serverapp import ServerApp
from flask import Flask, render_template_string

app = Flask(__name__)

# Đặt mật khẩu
os.environ['JUPYTER_LAB_PASSWORD'] = os.getenv('PASSWORD', 'your_default_password')

# Khởi động JupyterLab
def start_jupyter():
    server = ServerApp()
    server.launch_instance()

@app.route('/')
def index():
    port = os.environ.get('PORT', 8888)  # Lấy cổng từ biến môi trường
    start_jupyter() # Khởi động JupyterLab khi truy cập trang chủ
    return render_template_string(
        "JupyterLab đang chạy tại cổng: {{ port }}",
        port=port
    )

if __name__ == '__main__':
    app.run(debug=True)
