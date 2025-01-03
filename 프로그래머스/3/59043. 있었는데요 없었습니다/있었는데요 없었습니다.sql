# 1. 보호 시작일(B.DATETIME)보다 입양일(A.DATETIME) 더 빠른 동물의 '아이디', '이름'을 조회하는 SQL문을 작성
# 2. 결과는 보호 시작일이 빠른 순으로 조회

SELECT A.ANIMAL_ID, A.NAME FROM ANIMAL_INS A
JOIN ANIMAL_OUTS B ON A.ANIMAL_ID = B.ANIMAL_ID
WHERE B.DATETIME < A.DATETIME
ORDER BY A.DATETIME
