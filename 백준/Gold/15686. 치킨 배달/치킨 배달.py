def calc_dist(sel_ckns):
    # 선택된 치킨집들과 각 집 사이의 최소 거리 합산
    total_dist = 0
    for hx, hy in homes:  # 각 집 좌표 처리
        min_dist = 2 * N  # 초기 큰 값 설정
        for cx, cy in sel_ckns:  # 선택된 치킨집과의 거리 계산
            min_dist = min(min_dist, abs(hx - cx) + abs(hy - cy))
        total_dist += min_dist  # 최소 거리를 합산
    return total_dist  # 최종 치킨 거리 반환

def dfs(depth, sel_ckns):
    global answer
    # 남은 치킨집으로 M개를 못 채우는 경우 가지치기
    if len(sel_ckns) + (total_ckns - depth) < M:
        return
    
    # 모든 치킨집 탐색이 끝난 경우
    if depth == total_ckns:
        # 선택된 치킨집이 M개일 때만 치킨 거리 계산
        if len(sel_ckns) == M:
            answer = min(answer, calc_dist(sel_ckns))
        return

    # 치킨집 유지하는 경우
    dfs(depth + 1, sel_ckns + [chickens[depth]])
    # 치킨집 폐업하는 경우
    dfs(depth + 1, sel_ckns)

# N: 도시 크기, M: 선택할 치킨집 수
N, M = map(int, input().split())  
# 도시 정보 입력
city = [list(map(int, input().split())) for _ in range(N)]  

# 집과 치킨집 좌표 저장
homes = []
chickens = []
for i in range(N):
    for j in range(N):
        if city[i][j] == 1:  # 집
            homes.append((i, j))
        elif city[i][j] == 2:  # 치킨집
            chickens.append((i, j))
total_ckns = len(chickens)  # 치킨집 총 개수

# 최악의 경우를 대비한 최대 거리 설정
answer = 2 * N * 2 * N
# DFS 탐색 시작
dfs(0, [])  
# 최종 치킨 거리 최소값 출력
print(answer) 