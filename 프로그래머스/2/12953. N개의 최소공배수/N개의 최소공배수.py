import math

# 최소공배수 = 두수 곱한 것 나누기 최대공약수
def lcm(x, y):                 
    # gcd = 최대공약수는 두 수의 공통된 약수 중 가증 큰 수
    return x * y // math.gcd(x, y)       

def solution(arr):
    # 초기값 answer를 설정해야 num과 비교 가능
    answer = arr[0]       
    # arr[1:] 부터 시작해서 answer와 num 중 최소공배수 체크
    for num in arr[1:]:
        answer = lcm(answer, num)       
    return answer