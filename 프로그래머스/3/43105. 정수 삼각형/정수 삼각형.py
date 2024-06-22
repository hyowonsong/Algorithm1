def solution(triangle):
    # 삼각형의 높이
    height = len(triangle)
    
    # Bottom-up 방식으로 DP 배열을 초기화
    dp = triangle[-1]  # 맨 아래층의 값들을 초기값으로 설정
    
    # 맨 아래층부터 위층으로 올라가면서 최대 경로 합을 계산
    for i in range(height - 2, -1, -1):
        for j in range(i + 1):
            # 현재 위치 (i, j)에서의 최대 경로 합은
            # 아래층의 (i+1, j)와 (i+1, j+1) 중 큰 값과 현재 위치의 값 triangle[i][j]를 더한 값
            dp[j] = triangle[i][j] + max(dp[j], dp[j + 1])
    
    # dp[0]에는 최종적으로 꼭대기에서 바닥까지의 최대 경로 합이 저장됨
    return dp[0]
