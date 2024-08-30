from math import gcd
from functools import reduce

def solution(arrayA, arrayB):
    # 각 배열의 최대공약수를 구합니다.
    # reduce 함수를 사용하여 배열의 모든 요소에 대해 gcd를 순차적으로 적용
    gcdA = reduce(gcd, arrayA)
    gcdB = reduce(gcd, arrayB)
    
    # arrayB의 모든 원소가 gcdA로 나눠지는지 확인
    # 한쪽만 성립해야하기 때문에 둘다 성립되는 아래의 경우 return False 해준다.
    def check_divisibility(gcd_val, arrayX):
        for num in arrayX:
            if num % gcd_val == 0:
                return False
        return True

    answer = 0

    # gcdA가 arrayB의 모든 원소를 나누지 못하는 경우
    if check_divisibility(gcdA, arrayB):
        answer = max(answer, gcdA)
    
    # gcdB가 arrayA의 모든 원소를 나누지 못하는 경우
    if check_divisibility(gcdB, arrayA):
        answer = max(answer, gcdB)
    
    return answer