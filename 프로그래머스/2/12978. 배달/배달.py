from heapq import *

def solution(N, road, K):
    # 그래프 생성: 인접 리스트 방식
    graph = [[] for _ in range(N + 1)]  # 1번부터 N번 마을까지
    
    for a, b, c in road:
        graph[a].append((b, c))  # a에서 b로 가는 시간 c
        graph[b].append((a, c))  # b에서 a로 가는 시간 c (양방향)
    
    # 다익스트라 알고리즘 초기화
    distances = [float('inf')] * (N + 1)  # 최단 거리 배열 (1-indexed)
    distances[1] = 0  # 시작 마을은 거리 0
    queue = [(0, 1)]  # (현재까지의 거리, 현재 노드)
    
    while queue:
        current_distance, current_node = heappop(queue)
        
        # 이미 처리된 거리보다 큰 경우 무시
        if current_distance > distances[current_node]:
            continue
        
        # 연결된 노드들 탐색
        for neighbor, weight in graph[current_node]:
            distance = current_distance + weight
            if distance < distances[neighbor]:  # 더 짧은 경로를 발견한 경우
                distances[neighbor] = distance
                heappush(queue, (distance, neighbor))
    
    # K 시간 이하로 도달 가능한 마을 개수 반환
    count = 0
    # 모든 마을의 최단 거리를 확인합니다.
    for dist in distances[1:]:
        # 거리가 K 이하인 경우를 세어 count에 추가합니다.
        if dist <= K:
            count += 1
    
    # 배달이 가능한 마을의 수를 반환합니다.
    return count