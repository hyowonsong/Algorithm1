# 1. DOCTOR 테이블에서 진료과가 CS 이거나 GS인 의사의 이름, 의사 ID, 진료과, 고용 일자를 조회하는 SQL문
# 2. DATE_FORMAT 은 년, 월, 일 기준으로 내림차순 정렬하기 
# 3. 결과는 고용일자를 기준으로 내림차순 정렬하기
# 4. 고용일자가 같다면 이름을 기준으로 오름차순 정렬 

SELECT DR_NAME, DR_ID, MCDP_CD, DATE_FORMAT(HIRE_YMD, '%Y-%m-%d') FROM DOCTOR
WHERE MCDP_CD = 'CS' OR MCDP_CD = 'GS'
ORDER BY HIRE_YMD DESC, DR_NAME