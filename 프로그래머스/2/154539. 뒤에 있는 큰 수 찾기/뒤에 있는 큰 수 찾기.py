def solution(numbers):
    n = len(numbers)
    answer = [-1] * n  # 결과를 담을 리스트를 -1로 초기화
    
    stack = []  # 인덱스를 담을 스택
    
    for i in range(n):
        # 스택이 비어있지 않고, 현재 원소가 스택의 맨 위 원소보다 크면
        while stack and numbers[stack[-1]] < numbers[i]:
            idx = stack.pop()  # 스택에서 원소를 꺼내어
            answer[idx] = numbers[i]  # 해당 인덱스에 현재 원소를 뒷 큰수로 기록
        
        # 현재 원소의 인덱스를 스택에 추가
        stack.append(i)
    
    return answer