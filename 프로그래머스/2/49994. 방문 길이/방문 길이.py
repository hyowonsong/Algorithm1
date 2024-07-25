def solution(dirs):
    # 방향에 따른 좌표 변화를 정의
    # U: 위로, D: 아래로, R: 오른쪽으로, L: 왼쪽으로 이동
    moves = {'U': (0, 1), 'D': (0, -1), 'R': (1, 0), 'L': (-1, 0)}
    
    # 방문한 경로를 저장할 집합
    # (x1, y1, x2, y2) 형식으로 저장하며, (x1, y1)에서 (x2, y2)로의 이동을 의미
    visited = set()
    
    # 현재 위치 초기화
    # 시작점은 (0, 0)
    x, y = 0, 0
    
    # 처음 걸어본 길의 길이를 저장할 변수
    answer = 0
    
    # 입력된 각 방향 명령어에 대해 반복
    for i in dirs:
        # 다음 위치 계산
        # 현재 위치 (x, y)에서 moves[i]에 따라 이동한 좌표 (nx, ny) 계산
        nx, ny = x + moves[i][0], y + moves[i][1]
        
        # 경계를 벗어나지 않는 경우에만 이동
        if -5 <= nx <= 5 and -5 <= ny <= 5:
            # 현재 위치에서 다음 위치로의 경로
            path = (x, y, nx, ny)
            # 그 반대 경로 (반대로 이동하는 경우도 고려)
            reverse_path = (nx, ny, x, y)
            
            # 이 경로를 처음 걸어보는 경우
            if path not in visited and reverse_path not in visited:
                # 경로를 방문한 것으로 기록
                visited.add(path)
                visited.add(reverse_path)
                # 처음 걸어본 길이므로 길이 1 추가
                answer += 1
            
            # 위치 업데이트
            x, y = nx, ny
    
    # 처음 걸어본 길의 길이를 반환
    return answer
