from collections import deque

def bfs(computers, visited, start):
    # 시작점 노드를 큐에 추가하고 방문 처리합니다.
    queue = deque([start])
    visited[start] = True
    
    while queue:
        # 큐에서 현재 노드를 꺼냅니다.
        current = queue.popleft()
        # 현재 노드와 연결된 모든 노드를 탐색합니다.
        for i in range(len(computers)): 
            # 현재 노드와 i번째 노드가 연결되어 있고, i번째 노드를 아직 방문하지 않았다면
            if computers[current][i] == 1 and not visited[i]:
                # i번째 노드를 큐에 추가하고 방문 처리합니다.
                queue.append(i)
                visited[i] = True

def solution(n, computers):
    answer = 0
    # 각 노드의 방문 여부를 저장하는 리스트를 초기화합니다.
    visited = [False] * n
    
    # 모든 노드를 순회합니다.
    for i in range(n):
        # 만약 현재 노드를 아직 방문하지 않았다면
        if not visited[i]:
            # BFS를 통해 연결된 모든 노드를 방문 처리합니다.
            bfs(computers, visited, i)
            # 새로운 네트워크를 찾았으므로 네트워크의 수를 증가시킵니다.
            answer += 1
            
    return answer
