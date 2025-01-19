# 승리 조건 확인 함수
def check_winner(board, player):
    # 가로, 세로 검사
    for i in range(3):
        # 가로 검사
        if board[i][0] == player and board[i][1] == player and board[i][2] == player:
            return True
        # 세로 검사
        if board[0][i] == player and board[1][i] == player and board[2][i] == player:
            return True
    # 대각선 검사
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        return True
    if board[0][2] == player and board[1][1] == player and board[2][0] == player:
        return True
    return False

# 틱택토 상태 확인 함수
def solution(board):
    # "O"와 "X"의 개수 세기
    o_count = 0
    x_count = 0
    for row in board:
        o_count += row.count('O')
        x_count += row.count('X')
    
    # "O"와 "X"의 승리 여부 확인
    o_win = check_winner(board, 'O')
    x_win = check_winner(board, 'X')
    
    # 조건 확인
    # 1. "X"가 "O"보다 많을 수 없음
    if x_count > o_count:
        return 0
    # 2. "O"가 "X"보다 2개 이상 많을 수 없음
    if o_count > x_count + 1:
        return 0
    # 3. 둘 다 승리할 수 없음
    if o_win and x_win:
        return 0
    # 4. "O" 승리 시 "O"가 1개 더 많아야 함
    if o_win and o_count != x_count + 1:
        return 0
    # 5. "X" 승리 시 "O"와 "X" 개수가 같아야 함
    if x_win and o_count != x_count:
        return 0
    
    # 유효한 상황
    return 1