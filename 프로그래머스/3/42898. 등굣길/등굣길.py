def solution(m, n, puddles):
    # 한 열 DP 배열 초기화 (행과 열을 바꿔서 처리)
    dp = [0] * (m + 1)
    dp[1] = 1  # 집의 위치는 1로 초기화
    
    # DP 테이블 갱신
    for i in range(1, n + 1):
        temp = [0] * (m + 1)  # 현재 행의 임시 배열
        for j in range(1, m + 1):
            if i == 1 and j == 1:  # 집 위치
                temp[j] = 1
                continue
            if [j, i] in puddles:  # 물에 잠긴 지역
                temp[j] = 0
            else:
                temp[j] = (dp[j] + temp[j-1]) % 1000000007
        dp = temp  # 현재 행의 결과를 dp에 복사
    
    return dp[m]