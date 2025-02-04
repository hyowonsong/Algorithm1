def solution(dirs):
    # 캐릭터의 시작 위치
    x, y = 0, 0
    # 방문한 경로를 기록할 집합(중복 처리를 위해 set에 저장)
    visited = set()  
    # 각 명령에 따른 좌표 변화
    move_dict = {'U': (0, 1), 'D': (0, -1), 'R': (1, 0), 'L': (-1, 0)}
    
    for dir in dirs:
        # 이동할 방향
        dx, dy = move_dict[dir]
        # 새로운 위치
        nx, ny = x + dx, y + dy
        
        # 경계 밖으로 나가지 않도록 처리
        if -5 <= nx <= 5 and -5 <= ny <= 5:
            # 지나간 경로를 (x, y) -> (nx, ny) 형태로 기록
            if (x, y, nx, ny) not in visited and (nx, ny, x, y) not in visited:
                visited.add((x, y, nx, ny))  # 방문한 경로 추가
            # 캐릭터 위치 업데이트
            x, y = nx, ny
    
    # 방문한 경로의 개수 반환
    return len(visited)