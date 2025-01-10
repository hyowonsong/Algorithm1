# 레버를 만나면 다시 처음부터 최단 거리를 계산하는 로직!

from collections import deque

def bfs(start, end, maps):
    n = len(maps)
    m = len(maps[0])
    visited = [[-1] * m for _ in range(n)]
    
    # 시작점의 좌표 찾기
    start_x, start_y = start
    visited[start_x][start_y] = 0
    
    # 상하좌우 이동
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    queue = deque([(start_x, start_y)])
    
    while queue:
        x, y = queue.popleft()
        
        if (x, y) == end:
            return visited[x][y]
            
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            # 맵 범위 내에 있고, 방문하지 않았고, 벽이 아닌 경우
            if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == -1 and maps[nx][ny] != 'X':
                visited[nx][ny] = visited[x][y] + 1
                queue.append((nx, ny))
    
    return -1

def solution(maps):
    n = len(maps)
    m = len(maps[0])
    
    # 시작점, 레버, 출구 위치 찾기
    start = lever = end = None
    for i in range(n):
        for j in range(m):
            if maps[i][j] == 'S':
                start = (i, j)
            elif maps[i][j] == 'L':
                lever = (i, j)
            elif maps[i][j] == 'E':
                end = (i, j)
    
    # 시작점에서 레버까지의 최단 거리
    to_lever = bfs(start, lever, maps)
    if to_lever == -1:
        return -1
        
    # 레버에서 출구까지의 최단 거리
    to_exit = bfs(lever, end, maps)
    if to_exit == -1:
        return -1
    
    # 전체 이동 거리 반환
    return to_lever + to_exit