@echo off
chcp 65001
REM 로컬 서버 실행 배치 파일

REM 현재 bat 파일 위치로 이동
cd /d %~dp0

echo 서버를 실행합니다...
python app.py

pause