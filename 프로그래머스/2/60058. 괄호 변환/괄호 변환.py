# 괄호 변환

# 1.소스 코드에 작성된 모든 괄호를 뽑아서 올바른 순서대로 배치된 괄호 문자열 알려줌
# 1-1. 균형잡힌 괄호 문자열 : '('의 개수와 ')'의 개수가 같다
# 1-2. 올바른 괄호 문자열 : '(' 와 ')'의 짝도 모두 맞을 경우

# "균형잡힌 괄호 문자열" p가 매개변수로 주어질 때, 
# 주어진 알고리즘을 수행해 "올바른 괄호 문자열"로 변환한 결과를 return


def split_balanced(w):
    # 문자열을 최소 단위의 "균형잡힌 괄호 문자열" u와 나머지 문자열 v로 분리
    count = 0  # '('와 ')'의 개수를 카운트
    for i, char in enumerate(w):
        if char == '(':
            count += 1  # '('이면 +1
        else:
            count -= 1  # ')'이면 -1
        if count == 0:  # '('와 ')'의 개수가 같아지면 균형잡힌 상태
            return w[:i+1], w[i+1:]  # u는 현재까지, v는 나머지
    return w, ""  # 기본적으로 반환 (안 쓰이는 경우는 없음)

def is_correct(u):
    # 문자열이 "올바른 괄호 문자열"인지 검사
    stack = []  # 괄호의 짝을 맞추기 위한 스택
    for char in u:
        if char == '(':
            stack.append(char)  # '('를 스택에 추가
        else:  # char == ')'
            if not stack:  # 스택이 비어있으면 짝이 맞지 않음
                return False
            stack.pop()  # 짝이 맞으면 '('를 제거
    return len(stack) == 0  # 스택이 비어있으면 올바른 문자열 

def solution(p):
    # 1. 입력이 빈 문자열인 경우, 빈 문자열을 반환
    if not p:
        return ""  # 입력 문자열이 비었으면 빈 문자열 반환
    
    # 2. 문자열 w를 두 "균형잡힌 괄호 문자열" u, v로 분리
    u, v = split_balanced(p)
    
    # 3. 문자열 u가 "올바른 괄호 문자열" 이라면
    if is_correct(u):
        # 3-1. 문자열 v에 대해 1단계부터 다시 수행
        return u + solution(v)  # u 뒤에 v를 변환한 결과를 붙여서 반환
    
    # 4. 문자열 u가 "올바른 괄호 문자열"이 아니라면
    else:
        # 4-1 ~ 4-3. 빈 문자열에 '('를 붙이고, v에 대해 재귀 수행 후 ')'를 붙임
        answer = '(' + solution(v) + ')'
        # 4-4. u의 첫 번째와 마지막 문자를 제거하고 나머지 문자열의 괄호 방향을 뒤집어서 붙임
        for char in u[1:-1]:  # 첫 번째와 마지막 문자 제외
            if char == '(':
                answer += ')'  # '('를 ')'로 뒤집기
            else:
                answer += '('  # ')'를 '('로 뒤집기
        # 4-5. 생성된 문자열 반환
        return answer