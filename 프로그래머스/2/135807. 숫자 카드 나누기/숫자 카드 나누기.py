from math import gcd
from functools import reduce

def solution(arrayA, arrayB):
    # 각 배열의 최대공약수를 구합니다.
    # reduce 함수를 사용하여 배열의 모든 요소에 대해 gcd를 순차적으로 적용합니다.
    gcd_A = reduce(gcd, arrayA)
    gcd_B = reduce(gcd, arrayB)
    
    # 약수를 찾고 조건을 확인하는 함수
    def find_max_divisor(gcd, array1, array2):
        divisors = []
        # gcd의 제곱근까지만 반복하여 효율적으로 약수를 찾습니다.
        for i in range(1, int(gcd**0.5) + 1):
            if gcd % i == 0:
                divisors.append(i)
                # i가 gcd의 제곱근이 아닌 경우, 대응되는 약수도 추가합니다.
                if i != gcd // i:
                    divisors.append(gcd // i)
        
        # 약수들을 내림차순으로 정렬합니다.
        divisors.sort(reverse=True)
        
        # 가장 큰 약수부터 조건을 만족하는지 확인합니다.
        for div in divisors:
            # array2의 모든 숫자가 div로 나누어 떨어지지 않아야 합니다.
            if all(num % div != 0 for num in array2):
                return div
        # 조건을 만족하는 약수가 없으면 0을 반환합니다.
        return 0
    
    # 각 경우에 대해 최대 약수를 찾습니다.
    # arrayA의 최대공약수로 arrayB를 나눌 수 없는 경우
    max_A = find_max_divisor(gcd_A, arrayA, arrayB)
    # arrayB의 최대공약수로 arrayA를 나눌 수 없는 경우
    max_B = find_max_divisor(gcd_B, arrayB, arrayA)
    
    # 두 경우 중 더 큰 값을 반환합니다.
    # 이 값이 철수가 가진 카드들의 숫자를 모두 나눌 수 있는 가장 큰 양의 정수가 됩니다.
    return max(max_A, max_B)