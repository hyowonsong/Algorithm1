import heapq  # 우선순위 큐를 사용하기 위해 heapq 모듈을 import합니다.

def solution(N, road, K):
    # 그래프를 인접 리스트로 표현합니다.
    # 그래프는 각 마을의 인덱스를 기준으로 연결된 마을과 도로의 시간을 저장합니다.
    graph = []
    for i in range(N + 1):
        graph.append([])

    
    # 도로 정보를 기반으로 그래프를 구성합니다.
    for a, b, c in road:
        # 마을 a와 b를 연결하는 도로 정보 (b, c)와 (a, c)를 그래프에 추가합니다.
        graph[a].append((b, c))
        graph[b].append((a, c))
    
    # Dijkstra's algorithm을 위한 초기화
    # 각 마을까지의 최단 거리를 무한대로 초기화합니다.
    distances = [float('inf')] * (N + 1)
    # 1번 마을에서 자신까지의 거리는 0으로 설정합니다.
    distances[1] = 0
    # 우선순위 큐를 초기화합니다. (거리, 마을 번호) 형태로 저장됩니다.
    priority_queue = [(0, 1)]  # 시작점은 1번 마을, 거리 0
    
    while priority_queue:
        # 우선순위 큐에서 가장 거리가 짧은 노드를 꺼냅니다.
        current_dist, current_node = heapq.heappop(priority_queue)
        
        # 꺼낸 노드의 현재 거리가 이미 최단 거리보다 크면 무시합니다.
        if current_dist > distances[current_node]:
            continue
        
        # 현재 노드와 연결된 이웃 마을에 대해 거리를 갱신합니다.
        for neighbor, weight in graph[current_node]:
            distance = current_dist + weight
            # 새로운 거리가 기존 거리보다 짧으면 거리 갱신 및 우선순위 큐에 추가합니다.
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))
    
    # K 이하의 배달이 가능한 마을 수를 계산합니다.
    count = 0
    # 모든 마을의 최단 거리를 확인합니다.
    for dist in distances[1:]:
        # 거리가 K 이하인 경우를 세어 count에 추가합니다.
        if dist <= K:
            count += 1
    
    # 배달이 가능한 마을의 수를 반환합니다.
    return count
