N, M = map(int, input().split())  # 방의 크기
x, y, d = map(int, input().split())  # 로봇 청소기의 위치 (x, y)와 방향 d
room = [list(map(int, input().split())) for _ in range(N)]  # 방의 상태 (0: 빈 칸, 1: 벽)

# 북, 동, 남, 서에 대한 방향 설정
# 북: 0, 동: 1, 남: 2, 서: 3
dx = [-1, 0, 1, 0]  # 행 이동 (북, 동, 남, 서)
dy = [0, 1, 0, -1]  # 열 이동 (북, 동, 남, 서)

# 현재 칸이 청소되었는지 여부를 기록할 visited 배열
visited = [[0] * M for _ in range(N)]
visited[x][y] = 1  # 처음 로봇이 위치한 곳을 청소

def turn_left(d):
    return (d - 1) % 4  # 왼쪽으로 90도 회전

cleaned_count = 1  # 청소한 칸의 개수

while True:
    moved = False
    # 4방향을 체크
    for _ in range(4):
        d = turn_left(d)  # 왼쪽으로 회전
        nx = x + dx[d]  # 회전한 방향으로 이동할 좌표
        ny = y + dy[d]
        
        if 0 <= nx < N and 0 <= ny < M and room[nx][ny] == 0 and visited[nx][ny] == 0:
            # 청소되지 않은 빈 칸이 있다면
            visited[nx][ny] = 1  # 청소
            cleaned_count += 1  # 청소한 칸의 개수 증가
            x, y = nx, ny  # 이동
            moved = True
            break
    
    if not moved:  # 네 방향 모두 청소할 수 없는 경우
        # 후진할 좌표 계산
        back = (d + 2) % 4  # 반대 방향으로 후진
        nx = x + dx[back]
        ny = y + dy[back]
        
        if room[nx][ny] == 1:  # 후진할 자리가 벽이면 종료
            break
        
        x, y = nx, ny  # 후진
    
# 청소한 칸의 개수 출력
print(cleaned_count)