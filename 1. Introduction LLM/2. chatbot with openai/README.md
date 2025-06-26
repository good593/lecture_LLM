---
style: |
  img {
    display: block;
    float: none;
    margin-left: auto;
    margin-right: auto;
  }
marp: true
paginate: true
---
# OpenAI를 이용한 Chatbot 예제 

---
## 가상환경
1. 챗봇 프로젝트 폴더로 이동
2. 가상환경 만들기
```shell 
uv venv .venv
```
3. 가상환경 접속
```shell 
.\.venv\Scripts\activate
```

---
## 챗봇 실행 
1. `.env_sample`을 이용해서 `.env`파일 생성 
2. `.env`파일에 `OPENAI_API_KEY` 입력 
3. streamlit 실행 
```shell
streamlit run chatbot.py
```

