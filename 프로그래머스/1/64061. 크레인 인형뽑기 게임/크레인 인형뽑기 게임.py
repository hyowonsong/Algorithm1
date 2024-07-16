def solution(board, moves):
    answer = 0
    stack = []  

    for i in moves:  # 크레인의 움직임을 순회
        for j in range(len(board)):  # 보드의 세로 길이만큼 반복
            if board[j][i-1] != 0:  # 현재 위치에 인형이 있다면
                stack.append(board[j][i-1])  # 해당 인형을 스택에 추가
                board[j][i-1] = 0  # 뽑은 인형의 위치를 0으로 변경

                if len(stack) > 1:  # 스택에 2개 이상의 인형이 있고
                    if stack[-1] == stack[-2]:  # 최근에 뽑은 두 인형이 같다면
                        stack.pop(-1)  # 스택에서 제거
                        stack.pop(-1)
                        answer += 2  # 사라진 인형 개수 증가
                break  # 인형을 뽑았으므로 다음 move로 넘어감

    return answer  # 사라진 인형의 총 개수 반환