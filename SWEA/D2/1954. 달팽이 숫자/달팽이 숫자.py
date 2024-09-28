# 달팽이 숫자

T = int(input())

dx = [0, 0, -1, 1]  
dy = [-1, 1, 0, 0]  


for t in range(1, T + 1):
    # N x N 
    n = int(input())
    
    # N x N 크기의 2차원 리스트(그래프)
    graph = [[0] * n for _ in range(n)]

    # 현재 위치 (x, y), 숫자 카운트(cnt), 현재 방향(dr)
    x, y, cnt, dr = 0, 0, 1, 0
    
    # 시작 위치에 1을 채운다.
    graph[x][y] = cnt
    cnt += 1

    # cnt가 n*n보다 작거나 같은 동안 반복 
    while cnt <= n * n:
        # 현재 방향에 따라 다음 위치(nx, ny)를 계산한다.
        nx, ny = x + dx[dr], y + dy[dr]
        
        # 다음 위치가 범위 내에 있고, 아직 숫자가 채워지지 않은 경우
        if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] == 0:
            # 다음 위치로 이동
            x, y = nx, ny
            # 현재 위치에 현재 숫자(cnt)를 채운다.
            graph[x][y] = cnt
            cnt += 1
        else:
            # 방향을 시계방향으로 전환
            dr = (dr + 1) % 4

    # 테스트 케이스 번호 출력
    print(f'#{t}')
    # 그래프의 각 행 출력
    for row in graph:
        print(*row)  # 행을 공백으로 구분하여 출력
