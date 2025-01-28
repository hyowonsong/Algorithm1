SELECT A.ANIMAL_ID, A.ANIMAL_TYPE, A.NAME FROM ANIMAL_OUTS A
JOIN ANIMAL_INS B ON A.ANIMAL_ID = B.ANIMAL_ID
WHERE 
    B.SEX_UPON_INTAKE LIKE 'Intact%' # 들어올 때 중성화되지 않은 동물
    AND (A.SEX_UPON_OUTCOME LIKE 'Spayed%' OR A.SEX_UPON_OUTCOME LIKE 'Neutered%') # 나갈 때 중성화
ORDER BY A.ANIMAL_ID
