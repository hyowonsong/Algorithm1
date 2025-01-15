def solution(park, routes):
    # 시작 위치 찾기
    n, m = len(park), len(park[0])  
    for i in range(n):  # n으로 변경된 세로 길이
        for j in range(m):  # m으로 변경된 가로 길이
            if park[i][j] == 'S':
                x, y = i, j
                break
    
    # 방향에 따른 이동 정의
    directions = {
        'N': (-1, 0),
        'S': (1, 0),
        'W': (0, -1),
        'E': (0, 1)
    }
    
    # 각 명령 실행
    for route in routes:
        direction, dist = route.split()
        dist = int(dist)
        
        # 이동할 위치 계산
        dx, dy = directions[direction]
        nx, ny = x, y
        
        # 경로 상에 장애물이 있는지 확인
        obstacle = False
        for i in range(1, dist + 1):
            nx, ny = x + dx * i, y + dy * i
            # 공원을 벗어나는지 확인
            if not (0 <= nx < n and 0 <= ny < m) or park[nx][ny] == 'X':
                obstacle = True
                break
        
        # 장애물이 없다면 이동
        if not obstacle:
            x, y = nx, ny
    
    return [x, y]