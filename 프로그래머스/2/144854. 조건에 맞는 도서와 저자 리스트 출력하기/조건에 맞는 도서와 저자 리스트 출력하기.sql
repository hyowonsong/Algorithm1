# 경제 카테고리에 속하는 도서들의 도서 ID, 저자명, 출판일 리스트를 출력하는 SQL문을 작성

SELECT B.BOOK_ID, A.AUTHOR_NAME, DATE_FORMAT(B.PUBLISHED_DATE, '%Y-%m-%d') AS PUBLISHED_DATE
FROM BOOK B
JOIN AUTHOR A ON B.AUTHOR_ID = A.AUTHOR_ID
WHERE B.CATEGORY = '경제'
ORDER BY B.PUBLISHED_DATE ASC;
