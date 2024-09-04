# 음식물 피하기

# 음식물들은 뭉치게 돼서 큰 음식물 쓰레기가 된다.
# 떨어진 음식물 중에 제일 큰 음식물만은 피해가려고 한다.

from collections import deque

# 입력 받기
n, m, k = map(int, input().split())

# 그래프 초기화
graph = []
for i in range(n):
    graph.append([0] * m)

# 음식물 정보 입력
for _ in range(k):
    r, c = map(int, input().split())
    graph[r-1][c-1] = 1  # 인덱스는 0부터 시작하므로 1을 빼줍니다

# 상, 하, 좌, 우 방향 정의
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    queue = deque([(x, y)])
    graph[x][y] = 0  # 방문 처리
    size = 1

    while queue:
        x, y = queue.popleft()
        
        # 네 방향 탐색
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            # 범위를 벗어나거나 음식물이 없는 경우 무시
            if nx < 0 or nx >= n or ny < 0 or ny >= m or graph[nx][ny] == 0:
                continue
            
            graph[nx][ny] = 0  # 방문 처리
            queue.append((nx, ny))
            size += 1

    return size

# 가장 큰 음식물 크기 찾기
max_size = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            max_size = max(max_size, bfs(i, j))

# 결과 출력
print(max_size)