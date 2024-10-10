# 특정 거리의 도시 찾기
# 1~N 번까지의 도시와 M개의 단방향 도로가 존재. 도로의 거리는 1
# 특정한 도시 X로부터 출발하여, 최단 거리가 K인 모든 도시의 번호 출력

from collections import deque

import sys
input = sys.stdin.readline

# 도시의 개수 N, 도로의 개수 M, 거리 정보 K, 출발 도시 번호 X
n,m,k,x = map(int,input().split())
# M개의 줄에 걸쳐서 두 개의 자연수 a,b 주어지며, 각 자연수는 공백
graph = [[] for _ in range(n + 1)]

# 모든 도로 정보 입력 받기
for _ in range(m):
    a, b = map(int, input().split())
    # graph[1] = [2,3] 이렇게 될 수 있다.
    graph[a].append(b)

# 모든 도시에 대한 최단 거리 초기화
distance = [-1] *(n+1)
# 출발 도시까지의 거리는 0으로 설정
distance[x] = 0 

# 너비 우선 탐색 수행
queue = deque([x])

while queue:
    # 1번 도시에서 출발, 큐에는 [1], distance[1] = 0
    now = queue.popleft()
    # 현재 도시에서 이동할 수 있는 모든 도시를 확인
    for next_node in graph[now]:
        # 아직 방문하지 않은 도시라면
        if distance[next_node] == -1:
            # 최단 거리 갱신
            distance[next_node] = distance[now] + 1
            queue.append(next_node)

# 최단 거리가 K인 모든 도시의 번호를 오름차순으로 출력
check = False
for i in range(1,n+1):
    if distance[i] == k:
        print(i)
        check = True

# 만약 최단 거리가 k인 도시가 없다면, -1 출력
# 만약 check가 True이면 -1을 출력하지 않고 종료됩니다. 
if check == False:
    print(-1)
