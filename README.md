# Whale_Image_Translate_LocalServer
네이버 웨일 브라우저 이미지 파일 번역용 로컬 서버

## 개요

네이버 웨일 브라우저에서 Pixiv, Hitoxx, 로컬 저장소 (file:///~) 이미지 등의 이미지 번역을 차단함.

이 중, 로컬 저장소 이미지를 번역하기 위한 **매우 간단한** 로컬 서버 프로그램.

## 사용법









## 추가사항
**네이버 웨일 브라우저에서 localhost (127.0.0.1)을 차단하였을 경우:**

`hosts` 파일을 수정해 가짜 도메인을 localhost로 포워딩.

예시로, 가짜 도메인 `whaleimagetranslate.localserver`로 포워딩.

1. `c:\Windows\System32\drivers\etc\hosts` 파일을 메모장 (관리자 권한)으로 열기.
2. 맨 아래에 다음 줄 추가:
```
127.0.0.1 whaleimagetranslate.localserver
```
4. 터미널에서 열린 서버 포트 `xxxx` 확인
5. 브라우저에서 `http://whaleimagetranslate.localserver:xxxx`로 접속
