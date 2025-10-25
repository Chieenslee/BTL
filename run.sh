#!/bin/bash

echo "Kích hoạt môi trường ảo..."
source venv/bin/activate

echo "Cài đặt dependencies..."
pip install -r requirements.txt

echo "Khởi động ứng dụng..."
python app.py
