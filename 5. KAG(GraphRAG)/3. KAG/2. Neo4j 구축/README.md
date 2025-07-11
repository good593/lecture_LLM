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
# Neo4j Sandbox 구축

---
### [단계1: Neo4j Sandbox 접속](https://sandbox.neo4j.com) 
![bg right w:500](./img/image.png)

---
### 단계2: Create
![alt text](./img/image-1.png)

---
### 단계3: Connection details(접속 정보)
![alt text](./img/image-2.png)

---
### 단계4: Connect via drivers(파이썬 접속 방법)
![alt text](./img/image-6.png)

---
### 단계5: Open
![alt text](./img/image-3.png)

---
![alt text](./img/image-4.png)

---
- 저장된 데이터 없음: No Nodes & No Edge

![alt text](./img/image-5.png)

---
# 데이터셋 임포트

---
### [단계1: data-importer 접속](https://data-importer.neo4j.io/)
- 생성된 DB의 접속 정보 사용

![bg right w:500](./img/image-7.png)

---
### 단계2: 파일 업로드 
![alt text](./img/image-8.png)

---
# Node 정의
![alt text](./img/image-9.png)

---
### 단계1: User
![w:950](./img/image-10.png)

---
### 단계2: Movie
![w:950](./img/image-11.png)

---
### 단계3: Genre
![w:950](./img/image-12.png)

---
### 단계4: Keyword
![w:950](./img/image-13.png)

---
# Edge 정의

---
### 단계1: user2movie
![w:950](./img/image-14.png)

---
### 단계2: movie2user
![w:950](./img/image-15.png)

---
### 단계3: genre2movie
![w:950](./img/image-16.png)

---
### 단계4: movie2genre
![w:950](./img/image-17.png)

---
### 단계5: keyword2movie
![w:950](./img/image-18.png)

---
### 단계6: movie2keyword
![w:950](./img/image-19.png)

---
# Nodes & Edges 적용

---
### 단계1: Run import
![w:950](./img/image-20.png)

---
![w:950](./img/image-21.png)

---
![w:900](./img/image-22.png)

---
### 단계2: 확인 on Neo4j Sandbox
![alt text](./img/image-23.png)

---
### 단계3: Node 확인 
![alt text](./img/image-24.png)

---
### 단계4: Edge 확인
![alt text](./img/image-25.png)


