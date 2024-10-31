# 2644 촌수계산

import sys
input = sys.stdin.readline
from collections import deque

def bfs(curr_node):                                     # bfs 정의
    queue = deque()
    queue.append(curr_node)
    while queue:
        x = queue.popleft()
        for i in graph[x]:
            if visited[i] == -1:                       # graph에 방문했을 때 -1이 나오면 
                visited[i] = visited[x] + 1            # 방문했던 노드에 +1
                queue.append(i)


n = int(input())
start, end = map(int,input().split())
graph = [[] for _ in range(n+1)]
visited = [-1 for _ in range(n+1)]
for _ in range(int(input())):
    a,b = map(int,input().split())
    graph[a].append(b)                                 # 양방향
    graph[b].append(a)
visited[start] = 0
bfs(start)
print(visited[end])