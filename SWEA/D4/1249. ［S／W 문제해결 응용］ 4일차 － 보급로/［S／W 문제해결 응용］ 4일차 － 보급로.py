from collections import deque
INF = 10000
def bfs(si,sj,ei,ej):
    # q = []
    q = deque()
    v = [[INF]*N for _ in range(N)]

    q.append((si,sj))
    v[si][sj]=arr[si][sj]

    while q:
        # ci,cj = q.pop(0)
        ci,cj = q.popleft()
        # 4방향, 범위내, 중복허용(이동할 위치의 비용보다 적은경우)
        for di,dj in ((-1,0),(1,0),(0,-1),(0,1)):
            ni,nj = ci+di, cj+dj
            if 0<=ni<N and 0<=nj<N and v[ni][nj]>v[ci][cj]+arr[ni][nj]:
                q.append((ni,nj))
                v[ni][nj] = v[ci][cj] + arr[ni][nj]
    return v[ei][ej]

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    arr = [list(map(int,input())) for _ in range(N)]

    ans = bfs(0,0,N-1,N-1)
    print(f'#{test_case} {ans}')