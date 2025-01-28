# 1. 자동차 종류가 '세단' 또는 'SUV'인 자동차 중 2022년 11월 1일 ~ 22년 11월 30일 까지 대여 가능하고
  # 할인율이 적용되는 대여 기간 종류로는 '7일 이상', '30일 이상', '90일 이상'이 있다.(7일 미만일 경우 x)
# 2. 대여 금액이 50만원 이상 200만원 미만인 자동차에 대해서 자동차 ID, 자동차 종류, 대여금액(FEE)리스트 출력
# 3. 대여 금액 기준 내림차순, 금액 같으면 자동차 종류 기준 오름차순, 종류까지 같으면 자동차 ID 기준 내림차순

SELECT C.CAR_ID, C.CAR_TYPE as CAR_TYPE,ROUND(C.DAILY_FEE*30*(100-P.DISCOUNT_RATE)/100) AS FEE
FROM CAR_RENTAL_COMPANY_CAR C
JOIN CAR_RENTAL_COMPANY_RENTAL_HISTORY H ON C.CAR_ID = H.CAR_ID
JOIN CAR_RENTAL_COMPANY_DISCOUNT_PLAN P ON C.CAR_TYPE = P.CAR_TYPE 
WHERE C.CAR_ID NOT IN ( 
    SELECT CAR_ID
    FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
    WHERE END_DATE >= '2022-11-01' AND START_DATE <= '2022-12-01'       
) AND P.DURATION_TYPE like '%30%' -- 대여 기간이 30일 이상인 것을 검색해야하므로
GROUP BY C.CAR_ID 
HAVING C.CAR_TYPE IN ('세단', 'SUV') AND (FEE >= 500000 AND FEE < 2000000) 
ORDER BY FEE DESC, CAR_TYPE, CAR_ID DESC