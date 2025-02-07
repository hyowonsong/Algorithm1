# 2번째 예시를 보고 그냥 정렬해서 풀면은 안되겠구나를 유추해야 한다. 

def solution(number, k):
    stack = []
    for num in number:
        # 현재 스택에 들어있는 숫자보다 num이 크면 제거하는 방식
        while k > 0 and stack and stack[-1] < num:
            stack.pop()
            k -= 1
        stack.append(num)
    
    # k가 0이 아니면 마지막에 k개만큼 제거한 후 결과 반환
    return ''.join(stack[:len(stack) - k])
