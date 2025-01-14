from collections import deque

def solution(places):
    result = []
    for place in places:
        result.append(check_place(place))
    return result

def check_place(place):
    # 응시자들의 위치를 찾습니다
    people = []
    for i in range(5):
        for j in range(5):
            if place[i][j] == 'P':
                people.append((i, j))
    
    # 각 응시자별로 거리두기를 확인합니다
    for person in people:
        if not check_distance(place, person[0], person[1]):
            return 0
    return 1

def check_distance(place, row, col):
    visited = [[False] * 5 for _ in range(5)]
    queue = deque([(row, col, 0)])  # (row, col, distance)
    visited[row][col] = True
    
    dx = [-1, 1, 0, 0]  # 상하좌우
    dy = [0, 0, -1, 1]
    
    while queue:
        x, y, dist = queue.popleft()
        
        # 현재 위치가 시작점이 아니고, 응시자가 있는 자리라면
        if dist > 0 and place[x][y] == 'P':
            # 맨해튼 거리가 2 이하라면 거리두기 위반
            if dist <= 2:
                return False
            
        # 맨해튼 거리가 2를 초과하면 더 이상 확인할 필요 없음
        if dist >= 2:
            continue
            
        # 상하좌우 탐색
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < 5 and 0 <= ny < 5 and not visited[nx][ny]:
                # 파티션이 있는 경우 더 이상 진행하지 않음
                if place[nx][ny] == 'X':
                    continue
                    
                visited[nx][ny] = True
                queue.append((nx, ny, dist + 1))
                
    return True