gears = [list(map(int, input().strip())) for _ in range(4)]

# 회전 횟수 입력
K = int(input())

# K번의 회전 명령을 처리
for _ in range(K):
    # 회전할 톱니바퀴 번호와 방향 입력
    num, direction = map(int, input().split())
    num -= 1  # 인덱스 조정

    # 회전 방향을 저장할 리스트
    rotate_directions = [0] * 4
    rotate_directions[num] = direction

    # 왼쪽 톱니바퀴 회전 여부 체크
    for i in range(num, 0, -1):
        if gears[i][6] != gears[i-1][2]:  # 맞닿은 극이 다르면
            rotate_directions[i-1] = -rotate_directions[i]  # 반대 방향 회전
        else:
            break

    # 오른쪽 톱니바퀴 회전 여부 체크
    for i in range(num, 3):
        if gears[i][2] != gears[i+1][6]:  # 맞닿은 극이 다르면
            rotate_directions[i+1] = -rotate_directions[i]  # 반대 방향 회전
        else:
            break

    # 톱니바퀴 회전 적용
    for i in range(4):
        if rotate_directions[i] == 1:  # 시계 방향
            gears[i] = [gears[i][-1]] + gears[i][:-1]  # 오른쪽으로 회전
        elif rotate_directions[i] == -1:  # 반시계 방향
            gears[i] = gears[i][1:] + [gears[i][0]]  # 왼쪽으로 회전

# 최종 점수 계산
score = 0
if gears[0][0] == 1:
    score += 1
if gears[1][0] == 1:
    score += 2
if gears[2][0] == 1:
    score += 4
if gears[3][0] == 1:
    score += 8

# 결과 출력
print(score)
