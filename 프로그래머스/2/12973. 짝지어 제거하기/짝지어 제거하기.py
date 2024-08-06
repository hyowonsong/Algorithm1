# 짝지어 제거하기(스택 사용!!)

def solution(s):
    answer = 0
    stack = []

    for i in range(len(s)):
        # 만약 stack에 아무것도 없으면 stack에 넣어준다.
        if len(stack) == 0: 
            stack.append(s[i])
            
        # stack의 마지막이랑 s[i] 랑 같으면 stack 빼준다.
        elif stack[-1] == s[i]: 
            stack.pop()
            
        else:
            stack.append(s[i])

    if len(stack) == 0:
        return 1
    else:
        return 0 