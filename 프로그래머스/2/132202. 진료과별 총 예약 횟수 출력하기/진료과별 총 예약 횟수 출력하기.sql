# 22년 5월에 예약한 환자 수를 진료과코드 별로 조회하는 SQL문을 작성

# 1. 컬럼명은 '진료과 코드', '5월예약건수'
# 결과는 진료과별 예약한 환주 수를 기준으로 오름차순
# 예약한 환자 수가 같다면 진료과 코드를 기준으로 오름차순

SELECT MCDP_CD AS "진료과코드", COUNT(*) AS "5월예약건수" FROM APPOINTMENT
WHERE YEAR(APNT_YMD) = 2022 AND MONTH(APNT_YMD) = 05
GROUP BY MCDP_CD
ORDER BY COUNT(*), MCDP_CD