# 조합

# 1. 자연수 N과 R 이 주어진다.
# 2. 이때의 N combination R의 값을 나눈 나머지

# N combination R 은 N!/(R! * (N-R)!) 로 계산해야
# 페르마의 소정리 정수 a 와 소수 p를 가져와 (단, a != p) 
# a^(p-1) = ㅁ * p + 1 로 항상 나머지가 1이 남는다.

MOD = 1234567891

def factorial(n):
    result = 1
    for i in range(2, n+1):
        result = (result * i) % MOD
    return result

def mod_inverse(a, p):
    return pow(a, p-2, p) # 파이썬 내장함수로 a^(p-2) % p

def combination(n, r):
    if r == 0 or n == r:
        return 1
    num = factorial(n)  # N!
    denom = (factorial(r) * factorial(n - r)) % MOD  # R!(N-R)!
    return (num * mod_inverse(denom, MOD)) % MOD  # 조합 공식과 모듈러 연산

T = int(input())
for t in range(1,T+1):
    N, R = map(int, input().split())
    
    result = combination(N, R)
    print(f'#{t} {result}')