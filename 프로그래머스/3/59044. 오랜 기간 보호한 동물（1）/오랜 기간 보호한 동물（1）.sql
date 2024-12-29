# 1. 아직 입양을 못 간 동물 중, 가장 오래 보호소에 있었던 3마리의 '이름'과 '보호 시작일'을 조회하는 SQL문
# 2. 결과는 보호 시작일 순으로 조회

SELECT B.NAME, B.DATETIME
FROM  ANIMAL_INS B
WHERE B.ANIMAL_ID NOT IN (SELECT ANIMAL_ID FROM ANIMAL_OUTS)
ORDER BY B.DATETIME ASC
LIMIT 3;

