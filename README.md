# Whale_Image_Translate_LocalServer
네이버 웨일 브라우저 이미지 파일 번역용 로컬 서버

## 개요

최근, 네이버 웨일 브라우저에서 Pixiv, Hitoxx, 로컬 저장소 (file:///~) 이미지 등의 이미지 번역을 차단함.

이 중, 로컬 저장소 이미지를 번역하기 위한 **매우 간단한** 로컬 서버 프로그램.

## 사용법

0. 우측 상단의 '<> Code' → 'Download ZIP' 눌러 코드 파일 다운로드 후 적절한 위치에 압축 해제

1. Python (https://www.python.org/downloads) 에서 Python 최신버전 설치.

2. `install_requirements.bat` 실행. (Flask 설치)

3. `run_server.bat` 실행.

4. 터미널에서 열린 서버 포트 `xxxxx` 확인.

5. `http://localhost:xxxxx` 또는 `http://127.0.0.1:xxxxx` 로 접속.








## 추가사항
**네이버 웨일 브라우저에서 localhost (127.0.0.1) 에서의 이미지 번역을 차단하였을 경우:**

`hosts` 파일을 수정해 가짜 도메인을 localhost (127.0.0.1) 로 포워딩.

예시 - 가짜 도메인 `whaleimagetranslate.localserver`로 포워딩:

1. `c:\Windows\System32\drivers\etc\hosts` 파일을 메모장으로 열기.
2. 맨 아래에 다음 줄 추가:
```
#Whale_Image_Translate_Server
127.0.0.1 whaleimagetranslate.localserver
```
3. 파일 형식은 모든 파일, 무 확장자 (.txt 없이) 로 저장

    >⚠️ 권한 오류 발생 시
    >
    >"이 위치에 저장 할 권한이 없습니다. 권한을 얻으려면 관리자에게 문의하십시오" 라는 팝업이 뜰 경우:
    >
    >'문서' 폴더에 임시 저장 후, `c:\Windows\System32\drivers\etc\hosts` 에 관리자 권한으로 덮어쓰기.

4. 터미널에서 열린 서버 포트 `xxxxx` 확인.
5. 브라우저에서 `http://whaleimagetranslate.localserver:xxxxx`로 접속.
