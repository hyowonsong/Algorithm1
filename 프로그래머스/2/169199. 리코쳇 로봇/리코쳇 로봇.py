from collections import deque

def solution(board):
    # 보드의 크기
    n = len(board)
    m = len(board[0])
    
    # 시작점과 도착점 찾기
    start = None
    end = None
    for i in range(n):
        for j in range(m):
            if board[i][j] == 'R':
                start = (i, j)
            elif board[i][j] == 'G':
                end = (i, j)
    
    # 방문 여부를 저장할 set
    visited = set()
    
    # 이동 방향 (상, 하, 좌, 우)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    def slide(x, y, dx, dy):
        """주어진 방향으로 미끄러져 이동한 최종 위치를 반환"""
        moves = 0
        while 0 <= x + dx < n and 0 <= y + dy < m and board[x + dx][y + dy] != 'D':
            x += dx
            y += dy
            moves += 1
        return x, y, moves
    
    # BFS를 위한 큐 초기화
    queue = deque([(start[0], start[1], 0)])  # (x, y, 이동 횟수)
    visited.add((start[0], start[1]))
    
    while queue:
        x, y, count = queue.popleft()
        
        # 목표 지점에 도달했다면 현재까지의 이동 횟수 반환
        if (x, y) == end:
            return count
        
        # 네 방향으로 이동 시도
        for dx, dy in directions:
            # 해당 방향으로 미끄러져 이동
            new_x, new_y, _ = slide(x, y, dx, dy)
            
            # 이미 방문한 위치라면 스킵
            if (new_x, new_y) in visited:
                continue
            
            # 새로운 위치 방문 처리 및 큐에 추가
            visited.add((new_x, new_y))
            queue.append((new_x, new_y, count + 1))
    
    # 목표 지점에 도달할 수 없는 경우
    return -1