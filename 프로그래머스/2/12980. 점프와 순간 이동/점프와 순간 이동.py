def solution(n):
    answer = 1
    while n > 1:
        answer += n % 2
        n = n // 2
    return answer