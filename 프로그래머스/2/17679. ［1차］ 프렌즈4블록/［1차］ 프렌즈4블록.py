def solution(m, n, board):
    # 문자열을 리스트로 변환
    board_list = []
    for row in board:
        board_list.append(list(row))
    
    answer = 0
    while True:
        # 제거할 블록 찾기
        remove = set()
        for i in range(m-1):
            for j in range(n-1):
                if (board_list[i][j] == board_list[i][j+1] == board_list[i+1][j] == board_list[i+1][j+1] != ' '):
                    remove.add((i,j))
                    remove.add((i,j+1))
                    remove.add((i+1,j))
                    remove.add((i+1,j+1))
        
        # 더 이상 제거할 블록이 없으면 종료
        if not remove:
            return answer
        
        # 블록 제거 및 카운트
        answer += len(remove)
        for i, j in remove:
            board_list[i][j] = ' '
        
        # 빈 공간 채우기
        for j in range(n):
            queue = []
            for i in range(m):
                if board_list[i][j] != ' ':
                    queue.append(board_list[i][j])
            
            for i in range(m-1, -1, -1):
                if len(queue) > 0:
                    board_list[i][j] = queue.pop()
                else:
                    board_list[i][j] = ' '

    return answer