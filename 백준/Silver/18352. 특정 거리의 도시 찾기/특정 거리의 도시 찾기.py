# 특정 거리의 도시 찾기
import sys
input = sys.stdin.readline
from collections import deque

# 도시의 개수, 도로의 개수, 거리 정보, 출발 도시의 번호 입력
n, m, k, x = map(int, input().split())

# 도로 정보를 저장할 리스트 초기화
road = [[] for _ in range(n + 1)]
# 방문 여부를 확인하는 리스트 초기화
visited = [False] * (n + 1)
# 출발 도시는 방문한 것으로 처리
visited[x] = True

# 도로 정보 입력 및 저장
for _ in range(m):
    a, b = map(int, input().split())
    # 단방향 도로를 road 리스트에 저장
    road[a].append(b)

# BFS로 최단 거리 찾기
result = [-1] * (n + 1)
result[x] = 0

def bfs(x, road):
    # 출발 도시를 큐에 넣고 시작
    queue = deque([x])
    while queue:
        v = queue.popleft()
        # 현재 도시와 연결된 도시들을 확인
        for i in road[v]:
            # 방문하지 않은 도시라면 방문 여부를 체크하고 거리 정보 갱신
            if not visited[i]:
                visited[i] = True
                result[i] = result[v] + 1
                queue.append(i)

# BFS 함수 호출
bfs(x, road)

# 찾고자 하는 거리에 해당하는 도시가 있는지 확인 후 출력
exist = False
for i in range(1, n+1):
    if result[i] == k:
        exist = True
        print(i)

# 찾고자 하는 거리에 해당하는 도시가 없으면 -1 출력
if not exist:
    print(-1)
