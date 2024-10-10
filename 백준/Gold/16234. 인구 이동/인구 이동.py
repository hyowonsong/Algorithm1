from collections import deque

# BFS 탐색을 위한 함수 정의
def bfs(si, sj):
    q = deque()

    # 큐에 시작 좌표 삽입
    q.append((si, sj))    
    # 방문 표시  
    v[si][sj] = 1           
    # 연합에 포함된 나라 리스트
    alst = [(si, sj)]       
    # 연합의 인구 총합
    total = arr[si][sj]        

    # 네 방향 이동을 나타내는 리스트
    dx = [-1, 0, 1, 0]  
    dy = [0, 1, 0, -1]  

    # BFS 탐색
    while q:
        x, y = q.popleft()  # 큐에서 현재 좌표 꺼내기
        # 상하좌우 네 방향으로 탐색
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 범위 내에 있고, 아직 방문하지 않았으며, 인구 차이가 조건에 맞는지 확인
            if 0 <= nx < N and 0 <= ny < N and v[nx][ny] == 0 and L <= abs(arr[x][y] - arr[nx][ny]) <= R:
                q.append((nx, ny))    # 큐에 추가
                v[nx][ny] = 1         # 방문 처리
                alst.append((nx, ny)) # 연합 리스트에 추가
                total += arr[nx][ny]     # 인구 총합에 더함
    
    # 연합이 형성된 경우 (2개 이상의 나라로 구성된 경우)
    if len(alst) > 1:
        for ti, tj in alst:
            arr[ti][tj] = total // len(alst)  # 연합에 속한 나라의 인구를 평균값으로 설정
        return 1  # 연합이 있었음을 나타냄
    return 0  # 연합이 없었음을 나타냄


# 입력 처리
N, L, R = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

ans = 0
while True:
    # 방문 여부를 확인하기 위한 2차원 리스트 초기화
    v = [[0] * N for _ in range(N)]

    # 연합이 발생했는지 여부를 저장
    flag = 0 

    # 모든 나라를 탐색하며 연합 형성
    for i in range(N):
        for j in range(N):
            # 아직 방문하지 않은 나라에 대해
            if v[i][j] == 0:  
                # BFS 탐색을 수행하고 연합이 있었다면 1 반환
                flag = max(flag, bfs(i, j))  
    
    # 연합이 발생하지 않았으면 종료
    if flag == 0:
        break
    # 연합이 발생한 경우 인구 이동 횟수 증가
    ans += 1  

print(ans)
