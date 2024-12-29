# 최대공약수 = a mod b 를 반복적으로 계산하여 b=0이 되는 순간 a를 반환

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return (a * b) // gcd(a, b)

def solution(arr):
    result = arr[0]
    for num in arr[1:]:
        result = lcm(result, num)
    return result