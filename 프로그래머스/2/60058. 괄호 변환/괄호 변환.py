def solution(p):
    # 1. 입력이 빈 문자열인 경우, 빈 문자열을 반환
    if not p:
        return ""
    
    # 2. 문자열 w를 두 "균형잡힌 괄호 문자열" u, v로 분리
    u, v = split_balanced(p)
    
    # 3. 문자열 u가 "올바른 괄호 문자열" 이라면
    if is_correct(u):
        # 3-1. 문자열 v에 대해 1단계부터 다시 수행
        return u + solution(v)
    
    # 4. 문자열 u가 "올바른 괄호 문자열"이 아니라면
    else:
        # 4-1 ~ 4-3
        answer = '(' + solution(v) + ')'
        # 4-4
        for char in u[1:-1]:
            if char == '(':
                answer += ')'
            else:
                answer += '('
        # 4-5
        return answer

def split_balanced(w):
    count = 0
    for i, char in enumerate(w):
        if char == '(':
            count += 1
        else:
            count -= 1
        if count == 0:
            return w[:i+1], w[i+1:]
    return w, ""

def is_correct(u):
    stack = []
    for char in u:
        if char == '(':
            stack.append(char)
        else:
            if not stack:
                return False
            stack.pop()
    return len(stack) == 0