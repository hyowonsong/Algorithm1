# 입력 받기
n = int(input())  # 지도의 크기 n을 입력 받음
graph = []  # 지도 정보를 저장할 2차원 리스트
num = []  # 각 단지에 속한 집의 수를 저장할 리스트

# 지도 정보 입력 받기
for i in range(n):
    graph.append(list(map(int, input())))  # 지도 정보 입력

# 상하좌우 방향 이동을 위한 좌표 설정
dx = [0, 0, 1, -1]  # x 좌표 이동: 제자리, 제자리, 오른쪽, 왼쪽
dy = [1, -1, 0, 0]  # y 좌표 이동: 위로, 아래로, 제자리, 제자리

count = 0  # 현재 단지에 속한 집의 수를 세는 변수
result = 0  # 총 단지 수를 저장할 변수

def dfs(x, y):
    # 지도 범위를 벗어나는 경우
    if x < 0 or x >= n or y < 0 or y >= n:
        return False

    # 현재 위치에 집이 있는 경우
    if graph[x][y] == 1:
        global count
        count += 1  # 집의 수 증가
        graph[x][y] = 0  # 방문한 집은 0으로 표시하여 재방문하지 않도록 함

        # 상하좌우로 이동하며 연결된 집 탐색
        for i in range(4):
            nx = x + dx[i]  # 다음 x 좌표
            ny = y + dy[i]  # 다음 y 좌표
            dfs(nx, ny)  # 재귀적으로 DFS 호출

        return True  # 하나의 단지 탐색 완료
    return False  # 집이 없거나 이미 방문한 경우

# 지도를 순회하며 DFS 탐색
for i in range(n):
    for j in range(n):
        # 집이 있는 위치에서 DFS 탐색을 시작
        if dfs(i, j) == True:
            num.append(count)  # 단지에 속한 집의 수를 저장
            result += 1  # 단지 수 증가
            count = 0  # 다음 단지를 위해 집의 수 초기화

# 결과 출력
num.sort()  # 각 단지에 속한 집의 수를 오름차순으로 정렬
print(result)  # 총 단지 수 출력

for i in range(len(num)):
    print(num[i])  # 각 단지에 속한 집의 수 출력