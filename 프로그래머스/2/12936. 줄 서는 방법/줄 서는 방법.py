# 줄 서는 방법

def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n-1)

def solution(n, k):
    # 사용할 수 있는 숫자들의 리스트
    numbers = list(range(1, n+1))
    # 결과를 저장할 리스트
    result = []
    # k를 0-based index로 변환 (k는 1-based로 주어짐)
    k = k-1
    
    while n > 0:
        # 현재 자릿수에서 가능한 경우의 수
        f = factorial(n-1)
        # 현재 자릿수에 들어갈 숫자의 인덱스
        index = k // f
        # 다음 k 값 계산
        k = k % f
        # 해당 인덱스의 숫자를 결과에 추가하고 numbers에서 제거
        result.append(numbers[index])
        numbers.pop(index)
        n -= 1
    
    return result