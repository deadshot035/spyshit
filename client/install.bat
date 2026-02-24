@echo off
rmdir %USERPROFILE%\AppData\Local\Perfs
mkdir %USERPROFILE%\AppData\Local\Perfs
copy files\main.py  %USERPROFILE%\AppData\Local\Perfs\
copy files\logger.py  %USERPROFILE%\AppData\Local\Perfs\
copy files\obj.pkl  %USERPROFILE%\AppData\Local\Perfs\
copy files\.env  %USERPROFILE%\AppData\Local\Perfs\
copy startup.bat "%APPDATA%\Microsoft\Windows\Start Menu\Programs\Startup\"
pip install -r requirements.txt