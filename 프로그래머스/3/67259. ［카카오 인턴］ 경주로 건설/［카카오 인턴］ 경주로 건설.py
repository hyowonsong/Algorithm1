from collections import deque

def solution(board):
    N = len(board)
    
    # 상, 하, 좌, 우 방향 (dx, dy)
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    # 각 방향별 최소 비용 저장 (3차원 배열)
    cost = [[[float('inf')] * 4 for _ in range(N)] for _ in range(N)]
    
    queue = deque()
    
    # 시작 지점에서 모든 방향(상, 하, 좌, 우)으로 초기화
    for i in range(4):
        queue.append((0, 0, i, 0))  # (x, y, 방향, 비용)
        cost[0][0][i] = 0
    
    while queue:
        x, y, direction, current_cost = queue.popleft()
        
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            
            # 범위 체크 및 벽 체크
            if 0 <= nx < N and 0 <= ny < N and board[nx][ny] == 0:
                # 같은 방향 → 직선 도로 비용, 방향 바뀜 → 코너 비용
                if direction == i:
                    new_cost = current_cost + 100  #같은 방향이면 직선 도로 비용 100원 추가
                else:
                    new_cost = current_cost + 600  #방향이 바뀌면 코너 비용 500원+도로 비용 100원 추가
                
                # 더 적은 비용으로 방문 시 갱신
                if cost[nx][ny][i] > new_cost:
                    cost[nx][ny][i] = new_cost
                    queue.append((nx, ny, i, new_cost))
    
    # 도착점(N-1, N-1)까지의 최소 비용 반환
    return min(cost[N-1][N-1])
