def solution(arr):
    stack = []
    for i in arr:
        if len(stack) == 0:
            stack.append(i)
        else:
            # 현재 요소가 answer의 마지막 요소와 같은지 확인
            if i == stack[-1]: 
                continue
            else:
                stack.append(i)
    return stack