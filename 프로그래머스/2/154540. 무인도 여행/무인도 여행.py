import sys
sys.setrecursionlimit(10**6)  # 재귀 깊이 한도를 늘려 런타임 에러 방지

def dfs(x, y, maps, visited):
    # 지도의 크기
    n = len(maps)
    m = len(maps[0])
    
    # 현재 위치가 지도를 벗어나거나 이미 방문했거나 바다인 경우 0 반환
    if (x < 0 or x >= n or y < 0 or y >= m or 
        visited[x][y] or maps[x][y] == 'X'):
        return 0
    
    # 현재 위치 방문 처리
    visited[x][y] = True
    
    # 현재 위치의 식량
    current = int(maps[x][y])
    
    # 상하좌우 이동 방향
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    # 상하좌우 탐색하며 연결된 땅의 식량 더하기
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        current += dfs(nx, ny, maps, visited)
    
    return current

def solution(maps):
    n = len(maps)
    m = len(maps[0])
    visited = [[False] * m for _ in range(n)]
    result = []
    
    # 모든 위치를 탐색
    for i in range(n):
        for j in range(m):
            # 방문하지 않은 땅을 발견하면 DFS 수행
            if not visited[i][j] and maps[i][j] != 'X':
                days = dfs(i, j, maps, visited)
                result.append(days)
    
    # 무인도가 없는 경우 [-1] 반환
    if not result:
        return [-1]
    
    # 결과를 오름차순으로 정렬하여 반환
    return sorted(result)