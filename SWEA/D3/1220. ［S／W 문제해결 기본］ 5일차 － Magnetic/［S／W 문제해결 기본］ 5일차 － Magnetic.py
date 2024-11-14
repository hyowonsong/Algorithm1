T = 10
for test_case in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    ans = 0
    arr_t = list(zip(*arr)) # 전치행렬 만들기
    for lst in arr_t:       # 행단위로 처리
        prev = 0
        for n in lst:
            if n != 0:
                if n==2 and prev==1:
                    ans += 1
                prev = n
    print(f'#{test_case} {ans}')