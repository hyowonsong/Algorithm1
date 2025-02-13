# FOOD_PRODUCT와 FOOD_ORDER 테이블에서 생산일자가 22년 5월인 식품들의 식품 ID, 식품 이름, 총매출 조회
# 총 매출을 기준으로 내림차순, 총매출이 같다면 식품 ID를 기준으로 오름차순 정렬

SELECT B.PRODUCT_ID, B.PRODUCT_NAME, SUM(B.PRICE * A.AMOUNT) AS TOTAL_SALES
FROM FOOD_PRODUCT B
JOIN FOOD_ORDER A ON A.PRODUCT_ID = B.PRODUCT_ID
WHERE A.PRODUCE_DATE BETWEEN '2022-05-01' AND '2022-05-31'
GROUP BY B.PRODUCT_ID, B.PRODUCT_NAME
ORDER BY TOTAL_SALES DESC, B.PRODUCT_ID;

