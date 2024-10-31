
def bfs(si, sj):
    # [1] q, v, ans[] 생성
    q = []
    ans = []

    # [2] 초기값 삽입 등 단위작업
    q.append((si,sj))
    v[si][sj]=1
    ans.append(arr[si][sj])     # 정답관련 처리

    while q:
        ci,cj = q.pop(0)
        # 4방향, 범위내, 미방문, 1차이나는 위치면..
        for di,dj in ((-1,0),(1,0),(0,-1),(0,1)):
            ni,nj = ci+di, cj+dj
            if 0<=ni<N and 0<=nj<N and v[ni][nj]==0 and (abs(arr[ci][cj]-arr[ni][nj])==1):
                q.append((ni,nj))
                v[ni][nj]=1
                ans.append((arr[ni][nj]))
    return min(ans), len(ans)   # 제일 작은 번호, 개수를 리턴

T = int(input())
for test_case in range(1,T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 방문 여부 체크용 2차원 리스트 초기화
    v = [[0] * N for _ in range(N)] 
    # 최솟값 초기화 (큰 값), 최대 이동 방 개수 초기화
    num, cnt = N * N, 0  
    for i in range(N):
        for j in range(N):
            # 미방문인 방에 대해 BFS 탐색 수행
            if v[i][j] == 0:  
                # 시작 방에서 BFS 탐색 결과 얻기
                tnum, tcnt = bfs(i, j)  
                # 가장 긴 이동 경로이거나, 길이가 같고 숫자가 더 작은 경우 갱신
                if cnt < tcnt or (cnt == tcnt and num > tnum):
                    # 결과 갱신
                    num, cnt = tnum, tcnt 
    print(f'#{test_case} {num} {cnt}')  
