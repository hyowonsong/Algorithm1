# 1.할머니가 기르던 개는 이름에 'el'이 들어간다.
# 2.이름에 "EL"이 들어가는 개의 아이디와 이름을 조회하는 SQL문을 작성
# 3. 결과는 이름 순으로 조회

SELECT ANIMAL_ID, NAME FROM ANIMAL_INS
WHERE NAME LIKE '%EL%'
AND ANIMAL_TYPE = 'Dog'
ORDER BY NAME ASC