import math

def lcm(x, y):                           # 최소공배수 = 두수 곱한 것 나누기 최대공약수
    return x * y // math.gcd(x, y)       # gcd = 최대공약수는 두 수의 공통된 약수 중 가증 큰 수

def solution(arr):
    answer = arr[0]           # 초기값 answer를 설정해야 num과 비교 가능
    for num in arr[1:]:
        answer = lcm(answer, num)       
    return answer
