def solution(n, money):
    # DP 배열 초기화
    dp = [0] * (n + 1)
    dp[0] = 1  # 0원을 만드는 방법은 1가지
    
    # 동전 순회
    for coin in money:
        for i in range(coin, n + 1):
            dp[i] += dp[i- coin]
            dp[i] %= 1_000_000_007  # 나머지 연산 적용
            
    return dp[n]