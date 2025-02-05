# 핵심은 인덱스를 가지는 리스트를 하나 따로 빼는 것 + -1을 미리 정의

def solution(numbers):
    answer = [-1] * len(numbers)  # 뒷 큰수 없으면 -1인 것을 미리 정의
    stack = []  # 인덱스를 담을 스택
    
    for i in range(len(numbers)):
        # stack이 비어 있지 않고 stack의 맨 마지막 인덱스의 numbers보다 numbers[i]가 크면
        # if stack을 사용하면 스택의 맨 위 값 한 개만 비교하고 끝납니다. 현재는 전부 비교해야 하기 때문에
        # while stack을 사용하면 됩니다. 
        while stack and numbers[stack[-1]] < numbers[i]:
            idx = stack.pop()  # 현재 스택을 pop
            answer[idx] = numbers[i]  # pop한 자리에 numbers[i]를 넣기
        
        # 현재 원소의 인덱스를 스택에 추가
        stack.append(i)
    
    return answer
