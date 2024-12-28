# ANIMAL_INS 테이블에 등록된 모든 테이블에 대해 
# 1. 각 동물의 아이디와 이름, 들어온 날짜 조회
# 2. 결과는 아이디 순

# DATEFORMAT 잘 생각!

SELECT ANIMAL_ID, NAME, DATE_FORMAT(DATETIME, '%Y-%m-%d') AS 날짜 
FROM ANIMAL_INS
ORDER BY ANIMAL_ID