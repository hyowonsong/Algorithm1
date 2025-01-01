def dfs(node, visited, computers):
    # 현재 노드를 방문 처리
    visited[node] = True
    # 현재 노드와 연결된 다른 노드를 탐색
    for neighbor in range(len(computers[node])):
        if computers[node][neighbor] == 1 and not visited[neighbor]:
            dfs(neighbor, visited, computers)

def solution(n, computers):
    visited = [False] * n  # 모든 컴퓨터를 방문하지 않은 상태로 초기화
    network_count = 0      # 네트워크 개수

    # 모든 컴퓨터를 탐색
    for node in range(n):
        if not visited[node]:  # 방문하지 않은 컴퓨터가 있으면
            dfs(node, visited, computers)  # DFS로 연결된 컴퓨터를 모두 방문 처리
            network_count += 1  # 새로운 네트워크 발견 시 증가

    return network_count