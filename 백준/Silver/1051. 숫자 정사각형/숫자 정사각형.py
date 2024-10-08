
n, m = map(int, input().split())
graph = [list(input().strip()) for _ in range(n)]

max_size = 1

# 모든 가능한 정사각형의 꼭짓점을 확인
# 여기 size를 잘 체크해줘야
for size in range(1, min(n, m) + 1):  # 정사각형의 크기
    for i in range(n - size + 1):  # 시작 행
        for j in range(m - size + 1):  # 시작 열
            # 정사각형의 꼭짓점 값 체크
            top_left = graph[i][j]
            top_right = graph[i][j + size - 1]
            bottom_left = graph[i + size - 1][j]
            bottom_right = graph[i + size - 1][j + size - 1]
            
            # 모든 꼭짓점이 같으면
            if top_left == top_right == bottom_left == bottom_right:
                max_size = max(max_size, size)

# 최대 정사각형의 크기 출력
print(max_size * max_size)