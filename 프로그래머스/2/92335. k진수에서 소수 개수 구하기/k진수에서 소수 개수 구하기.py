def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def solution(n, k):
    answer = 0
    converted = ''
    
    # n을 k진수로 변환
    while n > 0:
        # 현재 변환된 숫자의 앞에 추가하여 k진수 문자열을 만듭니다.
        converted = str(n % k) + converted
        # n을 k로 나눈 몫으로 갱신합니다. 이렇게 하면 다음 자릿값을 계산
        n //= k
    
    # 변환된 수에서 소수 찾기
    # k진수로 변환된 문자열을 0을 기준으로 분리
    tokens = converted.split('0')
    for token in tokens:
        if token == '':
            continue
        # 각 분리된 문자열이 소수인지 확인하고, 소수이면 answer를 1 증가
        if is_prime(int(token)):
            answer += 1
    
    return answer