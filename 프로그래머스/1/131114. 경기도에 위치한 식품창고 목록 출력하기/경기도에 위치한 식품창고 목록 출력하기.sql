# 1. 경기도에 위치한 창고의 ID, 이름, 주소, 냉동시설 여부 조회
# 2. 냉동시설 여부가 NULL 인 경우, 'N' 으로 출력
# 3. 결과는 창고 ID를 기준으로 오름차순

SELECT WAREHOUSE_ID, WAREHOUSE_NAME, ADDRESS, 
    CASE
        WHEN FREEZER_YN IS NULL THEN 'N'
        ELSE FREEZER_YN
    END AS FREEZER_YN FROM FOOD_WAREHOUSE
    WHERE ADDRESS LIKE '%경기%'
ORDER BY WAREHOUSE_ID 