### 회원가입/로그인 API 테스트까지 완료(02.17)
1. 회원가입 시 받아오는 정보

-> name, nickname, email, phone_num, child_name, child_birth, child_gender, password

2. 로그인 시 사용하는 필드명

 ->  nickname, password

3. 아이 생년월일 입력 받으면, 개월수 계산하는 함수 추가(age_in_months)


### Swagger API docs 완료!(02.17)
- http://127.0.0.1:8000/swagger
  - 위 페이지에서 문서와 API 테스트 진행 가능!
  - 대부분 API는 인증 필요, 사용자 인증을 먼저 진행해주세요!
- drf_yasg 설치해야 합니다.

### Flip detection POST 요청 처리 완료! (02.18)
- 다만 swagger api test는 아직 불완전합니다.
- 우선은 엔드포인트, request 형식 정도만 참고해주시고 POSTMAN을 계속 이용해주세요.
- Swagger 상의 Bearer 인증은 빠르게 완료하거나 아님 그냥 버리겠습니다(POSTMAN 좋네요).

### Swagger 상에서 바로 API 요청 가능! (02.20)
- 문서 상에서 바로 요청 가능합니다.
- *주의! -> Authorization에 토큰 입력 시 앞에 {Bearer + ' '}를 붙여주세요!
