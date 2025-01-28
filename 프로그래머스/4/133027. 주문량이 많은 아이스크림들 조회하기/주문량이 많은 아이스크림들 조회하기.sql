# FIRST_HALF(상반기 주분 정보) 테이블과 JULY(7월의 아이스크림 주문 정보) 테이블
# 7월 아이스크림 총 주문량과 상반기의 아이스크림 총 주문량을 더한 값이 큰 순서대로 상위 3개의 맛 조회

SELECT F.FLAVOR FROM FIRST_HALF F
JOIN JULY J ON F.FLAVOR = J.FLAVOR
GROUP BY F.FLAVOR
ORDER BY SUM(F.TOTAL_ORDER) + SUM(J.TOTAL_ORDER) DESC
LIMIT 3;
