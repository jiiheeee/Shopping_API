## Sharing Schedule_API 
### 소개
고객이 제품을 구매하기까지 필요한 기능 및 장바구니 편집 API

<br/>
<br/>
<br/>

## System Architecture
<img width="953" alt="스크린샷 2024-01-09 오후 6 24 29" src="https://github.com/jiiheeee/scheduler_API/assets/128598772/cff21b9c-50d9-4a7a-8686-905d2830afcc">

<br/>
<br/>
<br/>

## Database Diagrams
<img width="450" alt="스크린샷 2024-01-21 오후 3 18 55" src="https://github.com/jiiheeee/first_project/assets/128598772/5bf01b76-7c97-41ef-8bfb-b5d8b8ff1acb">


## 개발 환경
• 프로젝트는 다음 환경에서 개발 및 배포되었습니다

• 로컬환경:M1맥북

• 배포 환경: AWS ECS

<br/>
<br/>
<br/>

## 기술 스택
• Programming: Python3.10

• Framework: Django 5.0.1

• Dockerhub

<br/>
<br/>
<br/>

## API 명세
POST /signup 

POST /signin

<br/>

POST /reservation

GET /reservation

GET /reservation/{reservation_id} 

DELETE /reservation

<br/>

POST /payment

<br/>

POST /cart 

GET /cart 

PATCH /cart

DELETE /cart
