# 연구소

# N*M 크기 직사각형
# 빈칸(0), 벽(1), 바이러스(2)
# 세울 수 있는 벽의 개수는 3개
# 벽을 세운 뒤 안전 영역의 크기

# 전체 맵의 크기가 8*8이므로, 벽을 설치할 수 있는 모든 조합의 수는 최악의 경우 64C3
# 1. dfs 벽을 세워 준다 - 빈칸을 찾아서 벽을 세우고, count + 1로 재귀 호출
# 2. 벽이 3개 설치된 경우(재귀 탈출 조건) 
# 3. 바이러스 퍼뜨리기 (벽이 3개 설치되었으니 바이러스를 터뜨린다.)
# 4. 안전 영역 계산
# 5. 최댓값 갱신 및 백트레킹( 안전 영역의 크기를 최댓값과 비교하여 갱신)

n, m = map(int, input().split())
# 초기 맵 리스트
data = [list(map(int, input().split())) for _ in range(n)]
# 벽을 설치한 뒤의 맵 리스트
temp = [[0] *m for _ in range(n)]

# 4가지 이동 방향에 대한 리스트
dx = [-1,0,1,0]
dy = [0,1,0,-1]


# 결과값
result= 0

# 깊이 우선 탐색(DFS)을 이용해 각 바이러스가 사방으로 퍼지도록 하기
def virus(x, y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        # 상, 하, 좌, 우 중에서 바이러스가 퍼질 수 있는 경우
        if nx>=0 and nx<n and ny>=0 and ny<m:
            if temp[nx][ny] == 0:
                temp[nx][ny] = 2
                # 해당 위치에 바이러스 배치하고, 다시 재귀적으로 수행
                virus(nx,ny)

# 현재 맵에서 안전 영역의 크기 계산하는 메서드
def get_score():
    score = 0
    for i in range(n):
        for j in range(m):
            if temp[i][j] == 0:
                score += 1
    return score
    

# 깊이 우선 탐색(DFS)을 이용해 울타리를 설치하면서, 매 번 안전 영역의 크기 계산
def dfs(count):
    global result
    # 울타리가 3개 설치된 경우 
    if count == 3:
        for i in range(n):
            for j in range(m):
                # temp 에 data 그래프를 복사
                temp[i][j] = data[i][j]
        # 각 바이러스의 위치에서 전파 진행
        for i in range(n):
            for j in range(m):
                if temp[i][j] == 2:
                    virus(i,j)
        # 안전 영역의 최대값 계산
        result = max(result, get_score())
        return
    
    # 빈 공간에 울타리를 설치
    for i in range(n):
        for j in range(m):
            # 빈 공간인 경우 벽을 설치
            if data[i][j] == 0:
                data[i][j] = 1
                count += 1
                # 벽을 하나 세운 상태로 다시 DFS 재귀 호출
                dfs(count)
                # 원래 상태로 돌려놓기
                data[i][j] = 0
                # 벽을 다시 제거했으므로, 카운트 감소
                count -= 1

# 맨처음 dfs(0)을 수행
dfs(0)

print(result)