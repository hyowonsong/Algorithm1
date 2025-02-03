# 네트워크

def dfs(i, visited, computers):
    # 현재 노드를 방문 처리
    visited[i] = True
    # 현재 노드와 연결된 다른 노드를 탐색
    for neighbor in range(len(computers[i])):
        # start와 neighbor가 연결되어 있고 neighbor를 방문하지 않았더라면
        if computers[i][neighbor] == 1 and not visited[neighbor]:
            # 이웃인 neighbor 쪽을 방문한다. 
            dfs(neighbor, visited, computers)

def solution(n, computers):
    visited = [False] * n  # 모든 컴퓨터를 방문하지 않은 상태로 초기화
    answer = 0      # 네트워크 개수

    # 모든 컴퓨터를 탐색
    for i in range(n):
        if not visited[i]:  # 방문하지 않은 컴퓨터가 있으면
            dfs(i, visited, computers)  # DFS로 연결된 컴퓨터를 모두 방문 처리
            answer += 1  # 새로운 네트워크 발견 시 증가

    return answer