-- 고양이와 개는 몇 마리 있을까

# 1. 동물 보호소에 들어온 동물 중 고양이과 개가 각각 몇 마리

SELECT ANIMAL_TYPE , COUNT(ANIMAL_TYPE) AS count 
FROM ANIMAL_INS
GROUP BY ANIMAL_TYPE 
ORDER BY ANIMAL_TYPE
