def split_expression(expression):
    numbers = []
    operators = []
    temp = ""
    
    for char in expression:
        if char.isdigit():
            temp += char
        else:
            numbers.append(int(temp))
            operators.append(char)
            temp = ""
    numbers.append(int(temp))  # 마지막 숫자 추가
    
    return numbers, operators

def calculate(numbers, operators, priority):
    nums = numbers[:]
    ops = operators[:]
    
    # 우선순위 높은 순서대로 계산
    for op in priority:
        i = 0
        while i < len(ops):
            if ops[i] == op:
                if op == '+':
                    nums[i] = nums[i] + nums[i+1]
                elif op == '-':
                    nums[i] = nums[i] - nums[i+1]
                else:  # '*'
                    nums[i] = nums[i] * nums[i+1]
                
                nums.pop(i+1)
                ops.pop(i)
                i -= 1
            i += 1
    
    return abs(nums[0])

def make_priority(used, current, all_priorities, available):
    if len(current) == len(available):
        all_priorities.append(current[:])
        return
    
    for i in range(len(available)):
        if not used[i]:
            used[i] = True
            make_priority(used, current + [available[i]], all_priorities, available)
            used[i] = False

def solution(expression):
    # 수식 분리
    numbers, operators = split_expression(expression)
    
    # 사용된 연산자 종류 파악
    available = list(set(operators))
    
    # 가능한 모든 우선순위 조합 생성
    all_priorities = []
    used = [False] * len(available)
    make_priority(used, [], all_priorities, available)
    
    # 각 우선순위 조합에 대해 계산
    max_result = 0
    for priority in all_priorities:
        result = calculate(numbers, operators, priority)
        max_result = max(max_result, result)
    
    return max_result