# 1. '12세 이하'인 '여자환자'의 환자이름, 환자번호, 성별코드, 나이, 전화번호를 조회하는 SQL문을 작성
# 2. 전화번호가 없는 경우 'NONE'으로 출력시킨다.
# 3. 결과는 나이를 기준으로 내림차순 정렬
# 4. 나이가 같다면, 환자 이름을 기준으로 오름 차순 정렬

SELECT PT_NAME, PT_NO, GEND_CD, AGE, 
    CASE 
        WHEN TLNO IS NULL THEN 'NONE' 
        ELSE TLNO         
    END AS TLNO 
FROM PATIENT
WHERE GEND_CD = 'W' AND AGE<=12
ORDER BY AGE DESC, PT_NAME ASC
