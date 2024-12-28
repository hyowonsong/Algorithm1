# 보호소에서 몇 시에 입양이 가장 활발하게 일어나는지 확인
# 각 시간대별로 입양이 몇 건이나 발생했는지 조회하는 SQL문 작성

-- 코드를 입력하세요
SELECT HOUR(DATETIME) AS HOUR, COUNT(*) AS COUNT FROM ANIMAL_OUTS
WHERE HOUR(DATETIME) BETWEEN 9 AND 19
GROUP BY HOUR
ORDER BY HOUR