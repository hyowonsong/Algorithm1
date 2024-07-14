# 햄버거 만들기

def solution(ingredient):
    stack = []
    count = 0
    
    for item in ingredient:
        stack.append(item)
        
        # 스택의 길이가 4 이상이고, 마지막 4개 요소가 [1, 2, 3, 1]인 경우
        if len(stack) >= 4 and stack[-4:] == [1, 2, 3, 1]:
            # 햄버거 완성, 카운트 증가
            count += 1
            # 사용된 재료 제거 (pop 4번)
            for _ in range(4):
                stack.pop()
    
    return count