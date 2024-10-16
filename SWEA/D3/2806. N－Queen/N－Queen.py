def dfs(n):  
    global ans  
    # n이 N에 도달하면 모든 퀸을 배치한 것이므로 경우의 수 1 증가
    if n == N:
        ans += 1
        return

    # 현재 n번째 행에서 모든 열을 확인
    for j in range(N):
        # 열(v1), 좌상-우하 대각선(v2), 우상-좌하 대각선(v3) 체크
        if v1[j] == v2[n+j] == v3[n-j] == 0:
            # 퀸을 j열에 놓음 (각 배열에 1을 할당하여 표시)
            v1[j] = v2[n+j] = v3[n-j] = 1
            # 다음 행으로 이동하여 재귀 호출
            dfs(n+1)
            # 백트래킹: 퀸을 놓았던 자리를 다시 0으로 돌림
            v1[j] = v2[n+j] = v3[n-j] = 0


T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    # 퀸을 배치할 수 있는 경우의 수 초기화
    ans = 0

    # 열(v1), 좌상-우하 대각선(v2), 우상-좌하 대각선(v3)을 나타내는 배열 초기화
    # 각각의 배열 크기는 2*N로 설정 (대각선 체크를 위한 여유 공간 필요)
    v1, v2, v3 = [[0] * (2 * N) for _ in range(3)]

    # 첫 번째 행부터 퀸을 배치하는 dfs 호출
    dfs(0)

    print(f'#{test_case} {ans}')
