
# 100x100 도화지를 0으로 초기화
paper = [[0] * 100 for _ in range(100)]

# 색종이의 수 입력
n = int(input())

# 색종이 붙이는 위치 입력
for _ in range(n):
    x, y = map(int, input().split())
    
    # 색종이의 크기는 10x10이므로, 해당 좌표에서 10x10 영역을 1로 설정
    for i in range(x, x + 10):
        for j in range(y, y + 10):
            paper[i][j] = 1

# 검은 영역의 넓이 계산 (1로 표시된 부분을 카운트)
area = 0
for i in range(100):
    for j in range(100):
        if paper[i][j] == 1:
            area += 1

# 검은 영역의 넓이를 출력
print(area)