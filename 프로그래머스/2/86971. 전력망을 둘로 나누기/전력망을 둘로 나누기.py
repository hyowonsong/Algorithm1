from collections import defaultdict, deque

def solution(n, wires):
    
    def bfs(start, graph, visited):
        queue = deque([start])
        visited[start] = True
        count = 0
        
        while queue:
            node = queue.popleft()
            count += 1
            for neighbor in graph[node]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    queue.append(neighbor)
        
        return count
    
    min_difference = float('inf')
    
    # 전선 정보로 그래프 구축
    for i in range(len(wires)):
        graph = defaultdict(list)
        
        # 전선을 하나 끊고 나머지로 그래프를 만듭니다.
        for j in range(len(wires)):
            if i != j:
                v1, v2 = wires[j]
                graph[v1].append(v2)
                graph[v2].append(v1)
        
        # BFS를 사용하여 두 개의 네트워크로 분리된 후 노드 개수 세기
        visited = [False] * (n + 1)
        start_node = wires[i][0]  # 끊긴 전선의 첫 번째 노드에서 시작
        subtree_size = bfs(start_node, graph, visited)
        
        # 전체 n에서 subtree 크기를 빼면 다른 서브트리의 크기
        other_subtree_size = n - subtree_size
        
        # 두 서브트리의 크기 차이의 절대값 계산
        difference = abs(subtree_size - other_subtree_size)
        
        # 최소 차이 갱신
        min_difference = min(min_difference, difference)
    
    return min_difference
