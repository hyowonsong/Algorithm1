def solution(n):
    
    # dp 배열 초기화
    dp = [0] * (n + 1)
    
    # 초기 조건 설정
    dp[1] = 1
    if n > 1:
        dp[2] = 2
    
    # dp 배열 채우기
    for i in range(3, n + 1):
        dp[i] = (dp[i-1] + dp[i-2]) % 1000000007
    
    return dp[n]