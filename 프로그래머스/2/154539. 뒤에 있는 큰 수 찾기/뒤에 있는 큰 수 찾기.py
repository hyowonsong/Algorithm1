def solution(numbers):
    n = len(numbers)
    answer = [-1] * n  # 뒷 큰수 없으면 -1인 것을 미리 정의
    
    stack = []  # 인덱스를 담을 스택
    
    for i in range(n):
        # stack이 비어 있지 않고 stack의 맨 마지막보다 numbers[i]가 크면
        while stack and numbers[stack[-1]] < numbers[i]:
            idx = stack.pop()  # 현재 스택을 pop
            answer[idx] = numbers[i]  # answer idx 초기화
        
        # 현재 원소의 인덱스를 스택에 추가(while 문 안돌아도 추가됨)
        stack.append(i)
    
    return answer
