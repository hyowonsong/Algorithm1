# 빙고

# 5x5 크기의 빙고판 입력
bingo = [list(map(int, input().split())) for _ in range(5)]

# 사회자가 부를 25개의 수 입력
calls = [list(map(int, input().split())) for _ in range(5)]

# 빙고판에서 호출된 수를 0으로 바꾸는 함수
def mark_number(num):
    for i in range(5):
        for j in range(5):
            if bingo[i][j] == num:
                bingo[i][j] = 0  # 해당 숫자를 0으로 변경

# 빙고를 체크하는 함수
def check_bingo():
    line_count = 0
    
    # 가로 빙고 체크
    for row in bingo:
        if sum(row) == 0:
            line_count += 1
    
    # 세로 빙고 체크
    for col in range(5):
        if sum(bingo[row][col] for row in range(5)) == 0:
            line_count += 1
    
    # 대각선 빙고 체크 (왼쪽 위 -> 오른쪽 아래)
    if sum(bingo[i][i] for i in range(5)) == 0:
        line_count += 1
    
    # 대각선 빙고 체크 (오른쪽 위 -> 왼쪽 아래)
    if sum(bingo[i][4 - i] for i in range(5)) == 0:
        line_count += 1
    
    return line_count

# 사회자가 부르는 수 처리
count = 0
for i in range(5):
    for j in range(5):
        count += 1
        # 부른 숫자를 0으로 바꾸기
        mark_number(calls[i][j])  
        # 빙고가 3줄 이상 완성되었는지 확인
        if check_bingo() >= 3:    
            print(count)
            exit()  # 프로그램 종료