# 크레인 인형
def solution(board, moves):
    stack = []

    answer = 0
    # 맨 처음에는 moves를 기준으로 움직인다.(moves는 열이기 때문에 j)
    for j in moves:
        j = j-1 # 0-based index
        # 행을 한개씩 탐험하면서 
        for i in range(len(board)):
            # 거기에 0이 아닌 인형이 있다면
            if board[i][j] != 0:
                # 2가지 경우로 분류(stack의 맨 마지막과 같은 경우와 같지 않은 경우)
                pop_doll = board[i][j]
                board[i][j] = 0 # 해당 위치를 빈칸으로 설정
                # 맨 마지막과 같은 경우 stack에서도 빼주고 pop_doll도 0으로 변경
                if stack and stack[-1] == pop_doll:
                    answer += 2
                    stack.pop()
                else:
                    stack.append(pop_doll)
                # break는 인형을 꺼낸 후 더 이상 해당 열에서 진행하지 않기 위해 사용(중요!)
                break
    return answer