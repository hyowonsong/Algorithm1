# 가장 먼 노드

# 1. n개의 노드가 있는 그래프가 주어짐 (1부터 n까지 번호)
# 2. 1번 노드에서 가장 멀리 떨어진 노드의 갯수 구하기
# 2-1. 가장 멀리 떨어진 노드란 최단경로로 이동했을 때 간선의 개수가 가장 많은 노드들
# 노드의 개수 n, 간선에 대한 정보가 담긴 2차원 배열 vertex가 매개변수로 주어질 때, 1번 노드로부터 가장 멀리 떨어진 노드가 몇 개인지를 return하도록 solution함수를 작성

from collections import deque

def solution(n, vertex):
    # 그래프 초기화 (인접 리스트 방식)
    graph = [[] for _ in range(n + 1)]
    
    # 양방향 간선 정보 저장
    for a, b in vertex:
        graph[a].append(b)
        graph[b].append(a)
    
    # 각 노드까지의 거리를 저장할 배열
    # -1은 아직 방문하지 않은 상태를 의미
    distance = [-1] * (n + 1)
    
    # BFS 수행
    queue = deque([1])  # 1번 노드부터 시작
    distance[1] = 0  # 시작 노드의 거리는 0
    
    max_distance = 0  # 가장 먼 거리
    
    while queue:
        current = queue.popleft()
        
        # 현재 노드와 연결된 모든 노드 확인
        for i in graph[current]:
            # 아직 방문하지 않은 노드라면
            if distance[i] == -1:
                # 현재 노드의 거리 + 1을 저장
                distance[i] = distance[current] + 1
                queue.append(i)
                max_distance = max(max_distance, distance[i])
    
    # 가장 먼 거리를 가진 노드의 개수 계산
    return distance.count(max_distance)