def solution(number, k):
    stack = []  # 결과를 저장할 스택 초기화
    
    for i in range(len(number)):
        # i는 단순한 인덱스 번호로, 리스트의 실제 값이 아님
        # stack[-1] < i는 의미가 없음
        while k > 0 and stack and stack[-1] < number[i]:  # number[i]를 사용해야 함
            stack.pop()  # 스택에서 마지막 숫자 제거
            k -= 1  # 제거한 숫자 개수 감소
        
        # stack에 현재 숫자 추가
        stack.append(number[i])  # number[i]를 사용해야 함
    
    # 모든 숫자를 순회한 후에도 제거할 숫자가 남아있다면
    if k > 0:
        # stack의 처음부터 len(stack) - k번째 요소까지를 포함
        stack = stack[:-k]  
    
    # 스택의 숫자들을 문자열로 변환하여 반환
    return ''.join(stack)
