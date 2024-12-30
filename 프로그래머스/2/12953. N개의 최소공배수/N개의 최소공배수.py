# 최대공약수 = a mod b 를 반복적으로 계산하여 b=0이 되는 순간 a를 반환

def gcd(a, b):
    # b가 0이 되기전까지 while문은 돌아간다. 
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return (a * b) // gcd(a, b)

def solution(arr):
    # 맨 처음 arr[0]으로 하나 정하고 다음 숫자랑 계속 최소공배수 구하기
    answer = arr[0]
    for num in arr[1:]:
        answer = lcm(answer, num)
    
    return answer
