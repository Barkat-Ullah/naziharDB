@echo off
set "PATH=%LOCALAPPDATA%\Programs\Python\Python312;%LOCALAPPDATA%\Programs\Python\Python312\Scripts;%PATH%"
cd /d "%~dp0phython-programming"
python main.py
pause
