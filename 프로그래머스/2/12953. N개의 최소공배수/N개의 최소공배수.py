# N개의 최소공배수
# 입력된 두 수의 배수 중 공통이 되는 가장 작은 숫자

import math

def lcm(x, y):                           # 최소공배수 = 두수 곱한 것 나누기 최대공약수
    return x * y // math.gcd(x, y)       # gcd = 최대공약수는 두 수의 공통된 약수 중 가증 큰 수

def solution(arr):
    answer = arr[0]
    for num in arr[1:]:
        answer = lcm(answer, num)        # 둘 중에 최소공배수가 되는 것을 구하기
    return answer