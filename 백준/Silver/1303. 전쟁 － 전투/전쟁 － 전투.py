# 전투

# 우리 병사 = 흰색 옷(W)
# 적국 병사 = 파란색 옷(B)
# N명이 뭉쳐있을 때는 N^2의 위력
# 단, 같은 팀의 병사들이 대각선으로만 인접한 경우는 뭉쳐 있다고 보지 않는다.

# 입력 받기
N, M = map(int, input().split())
graph = [input().strip() for _ in range(M)]

visited = [[False] * N for _ in range(M)]

white_power = 0
blue_power = 0

# 방향 벡터 설정: 상, 하, 좌, 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y, color):
    # 시작점의 색깔과 같은 영역의 크기를 반환하는 함수
    stack = [(x, y)]
    count = 0
    while stack:
        x, y = stack.pop()
        if visited[x][y]:
            continue
        visited[x][y] = True
        count += 1
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < M and 0 <= ny < N and not visited[nx][ny] and graph[nx][ny] == color:
                stack.append((nx, ny))
    return count

# 전장을 순회하며 병사의 전투력 계산
for i in range(M):
    for j in range(N):
        if not visited[i][j]:
            if graph[i][j] == 'W':
                # 흰색 병사의 영역 크기 계산
                power = dfs(i, j, 'W')
                white_power += power * power
            else:
                # 파란색 병사의 영역 크기 계산
                power = dfs(i, j, 'B')
                blue_power += power * power

print(white_power, blue_power)