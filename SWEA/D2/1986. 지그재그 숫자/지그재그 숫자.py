T = int(input())

for t in range(1, T+1):
    n = int(input())
    answer = 0  # 각 테스트 케이스마다 0으로 초기화

    for i in range(1, n+1):
        if i % 2 == 0:  # 짝수는 뺀다
            answer -= i
        else:  # 홀수는 더한다
            answer += i

    print(f'#{t} {answer}')
