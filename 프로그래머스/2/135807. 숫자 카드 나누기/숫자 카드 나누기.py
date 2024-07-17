from math import gcd
from functools import reduce

def solution(arrayA, arrayB):
    # 각 배열의 최대공약수를 구합니다.
    gcd_A = reduce(gcd, arrayA)
    gcd_B = reduce(gcd, arrayB)
    
    # 약수를 찾고 조건을 확인하는 함수
    def find_max_divisor(gcd, array1, array2):
        divisors = []
        for i in range(1, int(gcd**0.5) + 1):
            if gcd % i == 0:
                divisors.append(i)
                if i != gcd // i:
                    divisors.append(gcd // i)
        
        divisors.sort(reverse=True)
        
        for div in divisors:
            if all(num % div != 0 for num in array2):
                return div
        return 0
    
    # 각 경우에 대해 최대 약수를 찾습니다.
    max_A = find_max_divisor(gcd_A, arrayA, arrayB)
    max_B = find_max_divisor(gcd_B, arrayB, arrayA)
    
    # 두 경우 중 더 큰 값을 반환합니다.
    return max(max_A, max_B)