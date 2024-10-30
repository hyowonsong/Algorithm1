def bfs(si, sj):
    # [1] q, v[] 생성
    q = []
    v = [[0]*N for _ in range(N)]

    # [2] q에 초기데이터 삽입, v표시
    q.append((si,sj))
    v[si][sj]=1

    while q:
        ci,cj = q.pop(0)
        if arr[ci][cj]==3:
            return 1    # 도착점에 도달했을 때 1 반환

        # 네방향, 범위내, 미방문, 벽이아니면 방문(q)
        for di,dj in ((-1,0),(1,0),(0,-1),(0,1)):
            ni,nj = ci+di, cj+dj
            if 0<=ni<N and 0<=nj<N and v[ni][nj]==0 and arr[ni][nj]!=1:
                q.append((ni,nj))
                v[ni][nj]=1
    return 0    # 도착점에 도달하지 못했을 때 0 반환

T = 10
for test_case in range(1, T + 1):
    tc = input()  # 테스트 케이스 번호 입력받기
    N = 16
    arr = [list(map(int,input())) for _ in range(N)]
    
    # 시작점과 도착점 찾기
    for i in range(N):
        for j in range(N):
            if arr[i][j]==2:
                si, sj = i, j
            if arr[i][j]==3:
                ei, ej = i, j

    ans = bfs(si, sj)
    print(f'#{test_case} {ans}')