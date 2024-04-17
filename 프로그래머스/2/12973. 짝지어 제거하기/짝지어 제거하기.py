# 짝지어 제거하기(스택 사용!!)

def solution(s):
    answer = 0
    stack = []

    for i in range(len(s)):
        if len(stack) == 0:
            stack.append(s[i])
        elif stack[-1] == s[i]:
            stack.pop()
        else:
            stack.append(s[i])

    if len(stack) == 0:
        return 1
    else:
        return 0 