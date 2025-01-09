# 두 숫자의 최대 공약수를 구하는 함수 (유클리드 알고리즘)
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# 배열의 숫자들로부터 최대 공약수를 계산하는 함수
def gcd_array(array):
    current_gcd = array[0]  # 배열의 첫 번째 요소를 초기 GCD로 설정
    for num in array[1:]:  # 두 번째 요소부터 반복하며 GCD를 계산
        current_gcd = gcd(current_gcd, num)
        if current_gcd == 1:  # GCD가 1이면 더 이상 계산할 필요 없음
            break
    return current_gcd

# 조건을 확인하는 함수
def validate(candidate, array):
    for x in array:
        if x % candidate == 0:  # candidate가 배열의 요소 중 하나라도 나누면 조건 불충족
            return False
    return True

# 메인 solution 함수
def solution(arrayA, arrayB):
    # 철수와 영희 각각의 배열에 대한 최대 공약수 계산
    gcdA = gcd_array(arrayA)
    gcdB = gcd_array(arrayB)

    max_a = 0

    # 철수의 최대 공약수가 영희 조건을 만족하는지 확인
    if validate(gcdA, arrayB):
        max_a = max(max_a, gcdA)

    # 영희의 최대 공약수가 철수 조건을 만족하는지 확인
    if validate(gcdB, arrayA):
        max_a = max(max_a, gcdB)

    return max_a
