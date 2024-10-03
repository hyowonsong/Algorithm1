# 100만 이하의 모든 소수

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def solution(n):
    primes = []  # 소수를 저장할 리스트
    for i in range(2, n + 1):
        if is_prime(i):
            primes.append(i)  # 소수일 경우 리스트에 추가
    return primes

# 100만 이하의 소수 구하기
n = 1000000
prime_numbers = solution(n)

# 결과 출력
print(" ".join(map(str, prime_numbers)))