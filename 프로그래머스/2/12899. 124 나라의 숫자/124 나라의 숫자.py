def solution(n):
    answer = ''
    while n > 0:
        n -= 1  # 1을 빼는 이유는 3으로 나눈 나머지 0, 1, 2를 1, 2, 4에 매핑하기 위함입니다.
        answer = '124'[n % 3] + answer
        n //= 3
    return answer