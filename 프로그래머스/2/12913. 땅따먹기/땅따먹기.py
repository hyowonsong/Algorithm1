def solution(land):
    # 첫 번째 행은 그대로 사용
    dp = land[0]
    
    # 두 번째 행부터 마지막 행까지 순차적으로 처리
    for i in range(1, len(land)):
        # 현재 행에서의 점수를 계산할 새로운 dp 배열
        new_dp = [0] * 4
        
        for j in range(4):
            # 현재 칸 j에서 얻을 수 있는 점수는, 이전 행에서 j와 다른 칸 중 최댓값을 더한 값
            new_dp[j] = max(dp[(j+1)%4], dp[(j+2)%4], dp[(j+3)%4]) + land[i][j]
        
        # dp 배열을 갱신
        dp = new_dp
    
    # 마지막 행에서 얻을 수 있는 최대 점수가 답
    return max(dp)
