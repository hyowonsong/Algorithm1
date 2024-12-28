# 1. 동물 보호소에 들어온 동물 중 젊은 동물의 아이디 + 이름을 조회
# 2. 결과는 아이디 순

SELECT ANIMAL_ID, NAME FROM ANIMAL_INS
WHERE INTAKE_CONDITION != 'Aged'
ORDER BY ANIMAL_ID