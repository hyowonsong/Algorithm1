# 아이디 순으로 조회
# NULL이라는 기호를 모르기 때문에 이름이 없는 동물은 "No name" 으로 표시

SELECT ANIMAL_TYPE,
    CASE 
        WHEN NAME IS NULL THEN 'No name' 
        ELSE NAME
    END AS NAME,
    SEX_UPON_INTAKE
FROM ANIMAL_INS
ORDER BY ANIMAL_ID ASC;

