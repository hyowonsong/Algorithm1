def solution(dirs):
    # 방향에 따른 좌표 변화를 정의
    moves = {'U': (0, 1), 'D': (0, -1), 'R': (1, 0), 'L': (-1, 0)}
    
    # 방문한 경로를 저장할 집합
    visited = set()
    
    # 현재 위치
    x, y = 0, 0
    
    # 처음 걸어본 길의 길이
    answer = 0
    
    for i in dirs:
        # 다음 위치 계산
        nx, ny = x + moves[i][0], y + moves[i][1]
        
        # 경계를 벗어나지 않는 경우에만 이동
        if -5 <= nx <= 5 and -5 <= ny <= 5:
            # 현재 위치에서 다음 위치로의 경로, 그리고 그 반대 경로
            path = (x, y, nx, ny)
            reverse_path = (nx, ny, x, y)
            
            # 이 경로를 처음 걸어보는 경우
            if path not in visited and reverse_path not in visited:
                visited.add(path)
                visited.add(reverse_path)
                answer += 1
            
            # 위치 업데이트
            x, y = nx, ny
    
    return answer