# 1. DEVELOPERS 테이블에서 FRONT END 스킬을 가진 개발자의 정보를 조회
# 2. 조건에 맞는 개발자의 ID, 이메일, 이름, 성을 조회하는 SQL문을 작성

# 비트 & 연산을 사용하면 자동으로 숫자가 2진수 비트로 바뀌어서 같은 부분을 찾아냅니다. 

SELECT DISTINCT D.ID, D.EMAIL, D.FIRST_NAME, D.LAST_NAME FROM DEVELOPERS D
JOIN SKILLCODES S ON (D.SKILL_CODE & S.CODE) = S.CODE
WHERE S.CATEGORY = 'Front End'
ORDER BY D.ID;
