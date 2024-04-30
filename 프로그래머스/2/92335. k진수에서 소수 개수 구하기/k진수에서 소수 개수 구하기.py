def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def solution(n, k):
    answer = 0
    converted = ''
    
    # n을 k진수로 변환
    while n > 0:
        converted = str(n % k) + converted
        n //= k
    
    # 변환된 수에서 소수 찾기
    tokens = converted.split('0')
    for token in tokens:
        if token == '':
            continue
        if is_prime(int(token)):
            answer += 1
    
    return answer