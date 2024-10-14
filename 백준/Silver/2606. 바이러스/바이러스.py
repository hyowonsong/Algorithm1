# 바이러스
n = int(input())  
v = int(input()) 

# 그래프 초기화 (n+1 크기로 설정, 1번부터 시작하기 때문)
graph = [[0] * (n+1) for _ in range(n+1)]

for i in range(v):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

visited = [0] * (n+1)

# DFS 함수
def dfs(v):
    visited[v] = 1  # 현재 노드 방문 처리
    count = 1  # 현재 노드도 감염된 컴퓨터로 포함
    for i in range(1, n+1):
        if not visited[i] and graph[v][i] == 1:  # 아직 방문하지 않았고, 연결된 경우
            count += dfs(i)  # 연결된 컴퓨터도 감염시키고 카운트 증가
    return count

# 1번 컴퓨터를 제외한 감염된 컴퓨터 수를 반환해야 하므로 -1
result = dfs(1) - 1
print(result)



