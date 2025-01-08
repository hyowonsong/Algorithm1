from collections import deque

def bfs(start, graph, visited):
    
    # 주어진 그래프에서 start 노드로부터 연결된 노드의 개수를 구함.
    queue = deque([start])
    visited[start] = True
    count = 1
    
    while queue:
        node = queue.popleft()
        for neighbor in graph[node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)
                count += 1
    return count


def solution(n, wires):
    # 전선을 하나씩 끊어가며 두 네트워크로 나눈 송전탑 개수의 최소 차이를 계산.
    min_difference = n  # 초기값을 최대값으로 설정
    
    for i in range(len(wires)):
        # 그래프 구성 (인접 리스트)
        graph = [[] for _ in range(n + 1)]
        for j, (v1, v2) in enumerate(wires):
            if i != j:  # 현재 제거된 전선 제외
                graph[v1].append(v2)
                graph[v2].append(v1)
        
        # 탐색
        visited = [False] * (n + 1)  # 방문 기록
        part1_size = bfs(1, graph, visited)  # 첫 번째 네트워크 크기
        part2_size = n - part1_size         # 두 번째 네트워크 크기
        
        # 최소 차이 업데이트
        min_difference = min(min_difference, abs(part1_size - part2_size))
    
    return min_difference