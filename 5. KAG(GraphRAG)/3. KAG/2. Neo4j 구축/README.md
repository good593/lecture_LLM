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
![bg right w:600](./img/image-1.png)

---
### 단계2: New Project
![alt text](./img/image-2.png)

---
![alt text](./img/image-3.png)

---
### 단계3: 생성된 DB의 접속 정보 확인 
![w:1000](./img/image-4.png)

---
# 데이터셋 임포트

---
### [단계1: data-importer 접속](https://data-importer.neo4j.io/)
- 생성된 DB의 접속 정보 사용

![bg right w:600](./img/image-5.png)

---
### 단계2: 파일 업로드 
![alt text](./img/image.png)

---
### 단계3: movieId 노드 생성
![alt text](./img/image-6.png)

---
### 단계4: rating 노드 생성
![alt text](./img/image-7.png)

---
### 단계5: userId 노드 생성
![alt text](./img/image-9.png)

---
### 단계6: genre 노드 생성
![alt text](./img/image-8.png)

---
### 단계7: keyword 노드 생성
![alt text](./img/image-10.png)

---
# 관계성 생성

---
### 단계1: Neo4j Sandbox 접속 
![alt text](./img/image-11.png)

---
### 단계2: Nodes 확인
![alt text](./img/image-12.png)

---
### 단계3: RATED 생성
```cypher
MATCH (r:rating), (u:userId {userId: r.userId}), (m:movieId {movieId: r.movieId})
MERGE (u)-[:RATED {score: r.rating}]->(m)
```
![alt text](./img/image-13.png)

---
```cypher
MATCH p=()-[r:RATED]->() RETURN p LIMIT 25
```
![alt text](./img/image-16.png)

---
### 단계4: HAS_GENRE 생성
```cypher
MATCH (m:movieId), (g:genre)
WHERE m.movieId = g.movieId
MERGE (m)-[:HAS_GENRE]->(g)
```
![alt text](./img/image-14.png)

---
```cypher
MATCH p=()-[r:HAS_GENRE]->() RETURN p LIMIT 25
```
![alt text](./img/image-17.png)

---
### 단계5: HAS_KEYWORD 생성
```cypher
MATCH (m:movieId), (k:keyword)
WHERE m.movieId = k.movieId
MERGE (m)-[:HAS_KEYWORD]->(k)
```
![alt text](./img/image-15.png)

---
```cypher
MATCH p=()-[r:HAS_KEYWORD]->() RETURN p LIMIT 25
```
![alt text](./img/image-18.png)



