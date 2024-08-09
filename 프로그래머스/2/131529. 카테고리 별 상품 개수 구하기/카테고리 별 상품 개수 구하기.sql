# 카테고리 별 상품 개수 구하기

# 1. 상품 별로 중복되지 않는 8자리 상품코드 값을 가지며, 앞 2자리는 카테고리 코드를 의미(앞 2자리이니까 LEFT 사용)
# 2. 상품 카테고리 코드별 상품 개수 출력
# 3. 카테고리 코드 기준 오름차순

SELECT LEFT(PRODUCT_CODE, 2) AS CATEGORY,
    COUNT(PRODUCT_ID) AS PRODUCTS
FROM PRODUCT
GROUP BY CATEGORY