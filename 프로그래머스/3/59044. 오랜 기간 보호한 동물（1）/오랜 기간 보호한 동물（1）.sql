# 1. 아직 입양을 못 간 동물 중, 가장 오래 보호소에 있었던 3마리의 '이름'과 '보호 시작일'을 조회하는 SQL문
# 2. 결과는 보호 시작일 순으로 조회
# 3. ANIMAL_OUTS테이블의 ANIMAL_ID는 ANIMAL_INS의 ANIMAL_ID 외래 키

SELECT B.NAME, B.DATETIME FROM ANIMAL_INS B
LEFT JOIN ANIMAL_OUTS A ON A.ANIMAL_ID = B.ANIMAL_ID
WHERE A.ANIMAL_ID IS NULL
ORDER BY B.DATETIME
LIMIT 3