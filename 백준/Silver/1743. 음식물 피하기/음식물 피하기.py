from collections import deque

# 입력 받기
n, m, k = map(int, input().split())

# 그래프 초기화 (m행 n열)
graph = []
for i in range(m):  # m개 행을 생성
    row = [False] * n  # 각 행의 열 수는 n
    graph.append(row)

# 음식물 정보 입력
for _ in range(k):
    r, c = map(int, input().split())
    graph[c-1][r-1] = True  # (r, c) -> (행, 열) -> (열, 행)로 인덱스 변환

# 상, 하, 좌, 우 방향 정의
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    queue = deque([(x, y)])
    graph[x][y] = False  # 방문 처리
    size = 1

    while queue:
        x, y = queue.popleft()
        
        # 네 방향 탐색
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            # 범위를 벗어나거나 음식물이 없는 경우 무시
            if nx < 0 or nx >= m or ny < 0 or ny >= n or not graph[nx][ny]:
                continue
                
            # True를 False로 방문 처리
            graph[nx][ny] = False  
            queue.append((nx, ny))
            size += 1

    return size

# 가장 큰 음식물 크기 찾기
max_size = 0
for i in range(m):  # 행의 수
    for j in range(n):  # 열의 수
        if graph[i][j]:
            max_size = max(max_size, bfs(i, j))

# 결과 출력
print(max_size)