T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    lst = list(map(int, input().split()))

    ans = s = 0
    while s < N:
        # 현재 구간에서 가장 높은 가격을 가진 날 찾기
        i_max = s
        for i in range(s + 1, N):
            if lst[i_max] < lst[i]:
                i_max = i
        
        # 구간 내에서 매수하여 i_max 날에 매도, 이익 계산
        for i in range(s, i_max):
            ans += (lst[i_max] - lst[i])
        
        # i_max 이후로 이동하여 다음 구간에서 반복
        s = i_max + 1

    print(f'#{test_case} {ans}')
