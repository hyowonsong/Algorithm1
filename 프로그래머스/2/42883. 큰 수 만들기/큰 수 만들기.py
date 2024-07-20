def solution(number, k):
    stack = []  # 결과를 저장할 스택 초기화
    
    for num in number:
        # k > 0: 아직 제거할 숫자가 남아있음
        # stack: 스택이 비어있지 않음
        # stack[-1] < num: 스택의 마지막 숫자가 현재 숫자보다 작음
        while k > 0 and stack and stack[-1] < num:
            stack.pop()  # 스택에서 마지막 숫자 제거
            k -= 1  # 제거한 숫자 개수 감소
        
        stack.append(num) 
    
    # 모든 숫자를 순회한 후에도 제거할 숫자가 남아있다면
    if k > 0:
        # 끝에서 k번째 요소를 제외한 모든 요소를 포함
        stack = stack[:-k]  
    
    # 스택의 숫자들을 문자열로 변환하여 반환
    return ''.join(stack)  