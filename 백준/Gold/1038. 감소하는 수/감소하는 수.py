from itertools import combinations

def generate_numbers():
    numbers = []
    
    digits = '9876543210'
    
    # 각 자릿수의 조합을 생성
    for length in range(1, 11):  # 최대 자릿수는 10
        for comb in combinations(digits, length):
            num = int(''.join(comb))
            if str(num) == ''.join(sorted(str(num), reverse=True)):
                numbers.append(num)
    
    # 결과를 오름차순으로 정렬
    return sorted(set(numbers))

def solution(N):
    numbers = generate_numbers()
    
    if N < len(numbers):
        return numbers[N]
    else:
        return -1

# 입력을 받고 N번째 감소하는 수를 찾음
N = int(input())
print(solution(N))
