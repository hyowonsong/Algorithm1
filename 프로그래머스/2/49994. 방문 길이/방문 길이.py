def solution(dirs):
    # 현재 위치 초기화
    x, y = 0, 0
    
    # 이미 방문한 길을 저장할 집합
    visited_paths = set()
    
    # 방향에 따른 이동 변화량
    direction_map = {
        'U': (0, 1),
        'D': (0, -1),
        'R': (1, 0),
        'L': (-1, 0)
    }
    
    for direction in dirs:
        # 이동할 위치 계산
        dx, dy = direction_map[direction]
        nx, ny = x + dx, y + dy
        
        # 좌표평면 경계를 넘어가는 경우 무시
        if -5 <= nx <= 5 and -5 <= ny <= 5:
            # 이동한 경로를 기록, 양방향 모두 기록
            path = ((x, y), (nx, ny))
            reverse_path = ((nx, ny), (x, y))
            
            if path not in visited_paths and reverse_path not in visited_paths:
                visited_paths.add(path)
                visited_paths.add(reverse_path)
            
            # 현재 위치 업데이트
            x, y = nx, ny
    
    # 처음 방문한 길의 수 반환
    return len(visited_paths) // 2