# DOCTOR 테이블에서 진료과가 CS이거나 GS인 의사 조회
# 결과는 고용일자(HIRE_YMD) 기준으로 내림차순
# 고용일자가 같다면 이름을 기준으로 오름차순

-- 코드를 입력하세요
SELECT DR_NAME, DR_ID, MCDP_CD, DATE_FORMAT(HIRE_YMD, '%Y-%m-%d') AS HIRE_YMD
FROM DOCTOR
# MCDP_CD 를 둘 다 명시해줘야
WHERE MCDP_CD = 'CS' OR MCDP_CD = 'GS'
# ORDER BY는 콤마로 계속 이어나갈 수 있음
ORDER BY HIRE_YMD DESC, DR_NAME ASC;