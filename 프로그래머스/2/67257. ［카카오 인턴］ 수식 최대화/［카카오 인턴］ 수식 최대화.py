# 수식 최대화

# 1. 참가자들에게는 숫자들과 3가지의 연산문자(+,-,*)만 전달된다.
# 2. 연산자의 우선순위를 자유롭게 재정의해 만들 수 있는 가장 큰 숫자를 제출
# 3. 만약 계산된 결과가 음수라면 해당 숫자의 절댓값으로 변환하여 제출
# 4. 숫자가 가장 큰 참가자를 우승자로 선정하며, 우승자가 제출한 숫자를 우승상금

# expression은 공백문자, 괄호문자 없이 오로지 숫자, 3가지 연산자만으로 이루어진 중위표기법

def split_expression(expression):
    # 숫자와 연산자를 분리하는 함수
    numbers = []  # 숫자를 저장할 리스트
    operators = []  # 연산자를 저장할 리스트
    temp = ""  # 현재 처리 중인 숫자를 임시로 저장할 문자열
    
    for char in expression:  # 수식의 각 문자를 순회
        if char.isdigit():  # 문자가 숫자인 경우
            temp += char  # 숫자를 임시 저장 문자열에 추가
        else:  # 문자가 연산자인 경우
            numbers.append(int(temp))  # 지금까지 저장된 숫자를 리스트에 추가
            operators.append(char)  # 연산자를 리스트에 추가
            temp = ""  # 임시 저장 문자열 초기화
    numbers.append(int(temp))  # 마지막 숫자를 리스트에 추가
    
    return numbers, operators  # 숫자 리스트와 연산자 리스트 반환

def calculate(numbers, operators, priority):
    # 주어진 연산자 우선순위에 따라 수식을 계산하는 함수
    nums = numbers[:]  # 숫자 리스트를 복사
    ops = operators[:]  # 연산자 리스트를 복사
    
    # 우선순위 높은 연산자부터 처리(all_priorities안에 priority가 있음)
    for op in priority:
        i = 0  # 현재 처리 중인 연산자의 인덱스
        while i < len(ops):  # 연산자 리스트를 순회
            if ops[i] == op:  # 현재 연산자가 우선순위에 해당하는 경우
                # 연산자에 따라 계산 수행
                if op == '+':
                    nums[i] = nums[i] + nums[i+1]  # 덧셈 수행
                elif op == '-':
                    nums[i] = nums[i] - nums[i+1]  # 뺄셈 수행
                else:  # op == '*'
                    nums[i] = nums[i] * nums[i+1]  # 곱셈 수행
                
                nums.pop(i+1)  # 계산된 다음 숫자를 제거
                ops.pop(i)  # 계산된 연산자를 제거
                i -= 1  # 인덱스 조정
            i += 1  # 다음 연산자로 이동
    
    return abs(nums[0])  # 최종 계산 결과의 절댓값 반환

def dfs(used, current, all_priorities, available):
    # 가능한 연산자 우선순위 조합을 생성하는 함수
    if len(current) == len(available):  # [결과] : 현재 조합이 모든 연산자를 포함하는 경우
        all_priorities.append(current[:])  # 조합을 결과 리스트에 추가
        return
    
    for i in range(len(available)):  # 사용 가능한 연산자를 순회
        if not used[i]:  # 아직 사용하지 않은 연산자인 경우
            used[i] = True  # 사용 표시
            dfs(used, current + [available[i]], all_priorities, available) # 재귀 호출로 연산자 추가
            used[i] = False  # 사용 표시 해제

def solution(expression):
    # 전체 문제 해결 함수
    # 1. 수식 분리
    numbers, operators = split_expression(expression)
    # 2. 사용된 연산자 종류 파악
    available = list(set(operators))  # 연산자의 중복 제거
    # 3. 가능한 모든 우선순위 조합 생성
    all_priorities = []  # 모든 우선순위 조합을 저장할 리스트
    used = [False] * len(available)  # 사용 여부를 체크하는 리스트
    dfs(used, [], all_priorities, available)
    # 4. 각 우선순위 조합에 대해 최대 결과값 계산
    max_result = 0  # 결과값의 최대치를 저장할 변수
    for priority in all_priorities:  # 모든 우선순위 조합을 순회
        result = calculate(numbers, operators, priority)  # 해당 우선순위로 계산
        max_result = max(max_result, result)  # 최대값 갱신
    
    return max_result  # 우승 상금(최대 결과값) 반환
