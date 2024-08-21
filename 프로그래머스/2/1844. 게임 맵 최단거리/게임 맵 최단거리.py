from collections import deque

def bfs(maps):
    n, m = len(maps), len(maps[0])
    # 상하좌우
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    queue = deque([(0, 0)])
    
    # queue가 빌 때까지 반복
    while queue:
        # x,y 나눠서 popleft() 해줘야
        x, y = queue.popleft()
        # 상하좌우 칸 확인하기
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            # 맵을 벗어나면 무시하기
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            # 벽이면 무시하기
            if maps[nx][ny] == 0:
                continue
            # 처음 지나가는 길이면 거리계산하고 다시 상하좌우 확인하기
            if maps[nx][ny] == 1:
                maps[nx][ny] = maps[x][y] + 1
                queue.append((nx, ny))
    
    # 상대 팀 진영(제일 오른쪽 아래 칸)까지의 거리 반환
    return maps[n-1][m-1]

def solution(maps):
    answer = bfs(maps)
    # 상대 팀 진영에 도착할 수 없을 때 -1
    if answer == 1 :
        return -1  
    else :
        return answer