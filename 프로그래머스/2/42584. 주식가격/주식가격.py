# 이 문제도 인덱스를 다루는 것이 핵심

def solution(prices):
    # 결과를 저장할 리스트를 0으로 초기화
    answer = [0] * len(prices)
    # 가격의 인덱스를 저장할 스택
    stack = []

    # 모든 가격을 순회
    for i in range(len(prices)):
        # 현재 가격이 스택의 마지막 가격보다 작다면, 가격이 떨어진 시점
        while stack and prices[stack[-1]] > prices[i]:
            top = stack.pop()  # 스택에서 인덱스를 꺼내고
            answer[top] = i - top  # 현재 인덱스에서 top의 인덱스를 빼기
        
        # stack이 비어 있으면 추가
        stack.append(i)
    
    # 루프가 끝난 이후 남아 있는 스택 처리
    for top in stack:
         # 끝까지 유지된 기간 계산 (len(prices)-1 은 한 몸이다.)
        answer[top] = len(prices) - 1 - top 

    return answer
