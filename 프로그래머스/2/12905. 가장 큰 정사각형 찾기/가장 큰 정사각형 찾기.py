def solution(board):
    n = len(board)      # 행의 개수
    m = len(board[0])   # 열의 개수
    
    # DP 테이블 초기화
    dp = [[0] * m for _ in range(n)]
    max_side = 0
    
    for i in range(n):
        for j in range(m):
            if board[i][j] == 1:
                # 첫 행이나 첫 열은 그대로 복사
                if i == 0 or j == 0:
                    dp[i][j] = 1
                else:
                    # 점화식 적용
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
                # 최대 변 길이 갱신
                max_side = max(max_side, dp[i][j])
    
    # 최대 변의 길이를 제곱하여 넓이를 반환
    return max_side ** 2
