from collections import deque

# 방향 전환
dx = [0, 1, 0, -1]  
dy = [1, 0, -1, 0]  

# 보드의 크기 입력
n = int(input())
# 사과의 개수 입력
k = int(input())

board = [[0] * n for _ in range(n)]

# 사과 위치 입력
for _ in range(k):
    a, b = map(int, input().split())
    board[a-1][b-1] = 1  

# 뱀의 방향 변환 정보 입력
L = int(input())
turn_info = []  # 방향 변환 정보 저장 리스트
for _ in range(L):
    second, turn = input().split()
    turn_info.append((int(second), turn))  # 방향 변환 정보를 튜플로 저장

# 게임 진행 함수
def simulate():
    # 처음에는 동쪽(오른쪽)을 향함
    direction = 0  
    # 총 경과 시간
    time = 0  
    # 뱀의 머리 위치 (초기 시작 위치)
    x, y = 0, 0  
    # 뱀의 위치를 2로 표시
    board[x][y] = 2  
    # 뱀의 몸을 큐로 관리
    snake = deque([(x, y)])  
    # 방향 변환 정보의 인덱스
    turn_idx = 0  

    while True:
        # 1초씩 진행
        time += 1
        # 뱀의 머리가 이동할 다음 위치 계산
        nx = x + dx[direction]
        ny = y + dy[direction]

        # 벽에 부딪히거나 자신의 몸에 부딪힌 경우 게임 종료
        if not (0 <= nx < n and 0 <= ny < n) or board[nx][ny] == 2:
            return time

        # 이동할 칸에 사과가 있는 경우
        if board[nx][ny] == 1:
            board[nx][ny] = 2  # 사과를 먹고 뱀의 머리 위치 갱신
            snake.append((nx, ny))  # 뱀의 몸을 늘림
        else:
            # 사과가 없는 경우, 이동 후 꼬리를 줄임
            board[nx][ny] = 2  # 머리를 이동한 곳으로 갱신
            snake.append((nx, ny))  # 뱀의 머리 추가
            tx, ty = snake.popleft()  # 꼬리를 제거
            board[tx][ty] = 0  # 꼬리가 있던 자리는 빈 칸으로 처리

        # 뱀의 머리를 새로운 위치로 갱신
        x, y = nx, ny

        # 방향 변환이 필요한 시간인 경우
        if turn_idx < L and time == turn_info[turn_idx][0]:
            if turn_info[turn_idx][1] == 'L':  # 왼쪽으로 회전
                direction = (direction - 1) % 4
            else:  # 오른쪽으로 회전
                direction = (direction + 1) % 4
            turn_idx += 1  # 다음 방향 변환 정보로 넘어감

# 결과 출력
print(simulate())
