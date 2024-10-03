T = int(input())  

for t in range(1, T+1):
    N = int(input())
    numbers = list(map(int, input().split()))  

    # 각 위치에서 끝나는 부분 수열의 길이를 저장 (최소 길이는 1)
    dp = [1] * N  

    for i in range(1, N):
        for j in range(i):
            if numbers[i] > numbers[j]:
                dp[i] = max(dp[i], dp[j] + 1)

    # 최장 증가 부분 수열의 길이 출력
    print(f'#{t} {max(dp)}')
