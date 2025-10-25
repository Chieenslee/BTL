@echo off
echo Kich hoat moi truong ao...
call venv\Scripts\activate.bat

echo Cai dat dependencies...
pip install -r requirements.txt

echo Khoi dong ung dung...
python app.py

pause
