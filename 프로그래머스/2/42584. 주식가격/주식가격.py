def solution(prices):
    answer = [0] * len(prices)  # 결과를 담을 리스트 초기화
    stack = []  # 가격의 인덱스를 담을 스택

    for i in range(len(prices)):
        # 스택이 비어있지 않고, 현재 가격이 스택의 맨 위 가격보다 작을 때
        while stack and prices[stack[-1]] > prices[i]:
            # 스택의 맨 위 가격 인덱스를 꺼내서
            top = stack.pop()
            # 현재 인덱스 i에서 스택의 맨 위 가격 인덱스 top을 빼면 가격이 떨어지지 않은 기간이 됨
            answer[top] = i - top
        
        # 현재 가격의 인덱스를 스택에 추가(stack에 아무것도 없을 때 사용이 된다.)
        stack.append(i)
    
    # 마지막 가격은 가격이 떨어지지 않은 기간이 없으므로 0으로 설정
    while stack:
        top = stack.pop()
        answer[top] = len(prices) - 1 - top
    
    return answer
