def solution(m, n, board):
    # 문자열을 리스트로 변환
    # 입력된 board는 문자열의 리스트이므로, 각 문자열을 리스트로 변환하여 2차원 리스트로 만듦
    board_list = []
    for row in board:
        board_list.append(list(row))
    
    # 제거한 블록 수를 저장할 변수 초기화
    answer = 0
    
    # 무한 반복, 더 이상 제거할 블록이 없을 때까지 계속 진행
    while True:
        # 제거할 블록의 좌표를 저장할 집합
        remove = set()
        
        # 모든 블록을 검사하여 2x2로 같은 블록이 모여있는지 확인
        for i in range(m-1):
            for j in range(n-1):
                # (i, j), (i, j+1), (i+1, j), (i+1, j+1) 블록이 모두 같고 빈 공간이 아닐 경우
                if (board_list[i][j] == 
                    board_list[i][j+1] == 
                    board_list[i+1][j] == 
                    board_list[i+1][j+1] != ' '):
                    
                    # 해당 블록들의 좌표를 제거 리스트에 추가
                    remove.add((i, j))
                    remove.add((i, j+1))
                    remove.add((i+1, j))
                    remove.add((i+1, j+1))
        
        # 더 이상 제거할 블록이 없으면 종료
        if not remove:
            return answer
        
        # 제거할 블록의 수만큼 카운트 추가
        answer += len(remove)
        
        # 제거된 블록을 표시하기 위해 ' ' (빈 공간)으로 변경
        for i, j in remove:
            board_list[i][j] = ' '
        
        # 각 열을 위에서 아래로 정리하기
        for j in range(n):
            # 1. 위에서부터 비어있지 않은 블록들만 임시로 보관
            queue = []
            for i in range(m):
                if board_list[i][j] != ' ':
                    queue.append(board_list[i][j])       
            # 2. 아래에서부터 다시 블록들을 쌓기
            for i in range(m-1, -1, -1):
                 # 쌓을 블록이 남아있으면 맨 마지막 블록부터 꺼내서 쌓기
                if len(queue) > 0:
                    board_list[i][j] = queue.pop()
                # 더 이상 쌓을 블록이 없으면 빈 공간으로 채우기
                else:
                    board_list[i][j] = ' '
    
    # 최종적으로 제거한 블록의 수 반환
    return answer
