def solution(board, moves):
    # 바구니를 초기화
    stack = []
    # 인형의 개수를 저장할 변수
    count = 0
    
    # moves 배열의 각 위치를 순회
    for move in moves:
        col = move - 1  # 0-based index로 변환
        # 맨 위에서 부터 하나씩 인형을 꺼내기
        for row in range(len(board)):
            if board[row][col] != 0:
                # 꺼낸 인형
                doll = board[row][col]
                # 해당 위치를 빈 칸으로 설정
                board[row][col] = 0
                # 스택에 인형 추가
                # 마지막 인형과 같은 경우 터트리기
                if stack and stack[-1] == doll:
                    stack.pop()  
                    count += 2  # 인형 두 개의 개수를 더함
                else:
                    stack.append(doll)
                break
    
    return count