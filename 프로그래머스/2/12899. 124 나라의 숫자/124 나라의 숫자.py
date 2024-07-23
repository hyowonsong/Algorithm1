def solution(n):
    answer = ''
    while n > 0:
        n -= 1  # 1을 빼는 이유는 3으로 나눈 나머지 0, 1, 2를 1, 2, 4에 매핑하기 위함입니다.
        answer = '124'[n % 3] + answer  # 나머지에 따라 1, 2, 4를 선택하여 문자열 앞에 추가합니다.
        n //= 3  # n을 3으로 나누어 다음 자릿수로 넘어갑니다.
    return answer
