# 사탕 게임

# 입력 처리
N = int(input())
board = [list(input().strip()) for _ in range(N)]

def solution(board, N):
    max_candies = 0
    
    # 각 행에서 최대 연속 길이를 계산
    for i in range(N):
        count = 1
        for j in range(1, N):
            if board[i][j] == board[i][j-1]:
                count += 1
            else:
                count = 1
            max_candies = max(max_candies, count)
    
    # 각 열에서 최대 연속 길이를 계산
    for j in range(N):
        count = 1
        for i in range(1, N):
            if board[i][j] == board[i-1][j]:
                count += 1
            else:
                count = 1
            max_candies = max(max_candies, count)
    
    return max_candies

def solve_candy_game(N, board):
    max_candies = 0
    
    for i in range(N):
        for j in range(N):
            # 오른쪽으로 교환
            if j + 1 < N and board[i][j] != board[i][j+1]:
                board[i][j], board[i][j+1] = board[i][j+1], board[i][j]
                max_candies = max(max_candies, solution(board, N))
                board[i][j], board[i][j+1] = board[i][j+1], board[i][j] # 원상복구
            
            # 아래쪽으로 교환
            if i + 1 < N and board[i][j] != board[i+1][j]:
                board[i][j], board[i+1][j] = board[i+1][j], board[i][j]
                max_candies = max(max_candies, solution(board, N))
                board[i][j], board[i+1][j] = board[i+1][j], board[i][j] # 원상복구
    
    return max_candies

# 결과 출력
print(solve_candy_game(N, board))