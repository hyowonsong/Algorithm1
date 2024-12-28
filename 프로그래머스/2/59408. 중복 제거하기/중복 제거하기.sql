# 동물 보호소에 들어온 동물의 이름은 몇 개인지 조회하는 SQL문을 작성
# 이름이 NULL 인 경우는 집게하지 않으며 중복되는 이름은 하나로 칩니다.

SELECT COUNT(DISTINCT NAME) FROM ANIMAL_INS
WHERE NAME IS NOT NULL