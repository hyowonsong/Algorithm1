T = int(input())
for test_case in range(1, T + 1):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    count = 0

    # 가로 방향 검사
    for i in range(N):
        rows_count = 0
        for j in range(N):
            if arr[i][j] == 1:
                rows_count += 1
            else:
                if rows_count == K:
                    count += 1
                rows_count = 0  # 1이 아니므로 초기화
        if rows_count == K:  # 마지막에 연속된 1이 K개면 count 증가
            count += 1

    # 세로 방향 검사
    for j in range(N):
        cols_count = 0
        for i in range(N):
            if arr[i][j] == 1:
                cols_count += 1
            else:
                if cols_count == K:
                    count += 1
                cols_count = 0  # 1이 아니므로 초기화
        if cols_count == K:  # 마지막에 연속된 1이 K개면 count 증가
            count += 1

    # 결과 출력
    print(f'#{test_case} {count}')
