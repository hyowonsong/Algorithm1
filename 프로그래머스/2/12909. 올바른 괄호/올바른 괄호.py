def solution(s):
    stack = []

    for i in s:
        if i == '(':  
            stack.append(i)
        elif i == ')' and stack and stack[-1] == '(':
            stack.pop()
        else:  
            return False

    # 스택이 비어있으면 True, 남아 있으면 False
    if len(stack) == 0:
        return True
    else:
        return False
