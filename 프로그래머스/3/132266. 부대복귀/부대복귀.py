from collections import deque 

def solution(n, roads, sources, destination):
    # 그래프 구성 (2차원 리스트)
    graph = [[] for _ in range(n + 1)]  
    for a, b in roads:  
        graph[a].append(b)  
        graph[b].append(a) 

    # 최단 거리 계산
    distances = [-1] * (n + 1)  
    distances[destination] = 0  # 목표 지역은 자기 자신까지 거리가 0
    queue = deque([destination])  # BFS 탐색을 위한 큐 초기화 (목표 지역에서 시작)
    
    while queue: 
        current = queue.popleft() 
        current_distance = distances[current]  # 현재 노드의 거리 가져오기
        
        for neighbor in graph[current]:  # 현재 노드의 인접 노드들을 확인
            if distances[neighbor] == -1:  # 아직 방문하지 않은 노드라면
                distances[neighbor] = current_distance + 1  # 현재 노드 거리 + 1로 설정
                queue.append(neighbor)  # 큐에 인접 노드 추가
    
    # 결과 생성
    result = []  
    for source in sources:  # sources 배열을 순회하며
        result.append(distances[source])  # 각 노드의 최단 거리를 결과 리스트에 추가
    
    return result  