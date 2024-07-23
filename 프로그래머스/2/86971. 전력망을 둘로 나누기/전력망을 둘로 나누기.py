# 전력망을 둘로 나누기(트리)

# 주어진 트리 구조에서 전선을 하나씩 끊어보고, 
# 두 개의 분리된 트리에서 송전탑의 개수를 계산하여 
# 두 트리의 송전탑 개수 차이를 최소화하는 전선을 찾으면 된다.

from collections import defaultdict

def solution(n, wires):
    # 최소 차이를 저장할 변수. 초기값은 가능한 최대 차이인 n으로 설정
    min_diff = n

    # 각 전선을 하나씩 끊어보며 모든 경우의 수를 검사
    for i in range(len(wires)):
        # 새로운 그래프를 생성. defaultdict를 사용해 키가 없을 경우 빈 리스트를 반환하도록 설정
        graph = defaultdict(list)
        
        # i번째 전선을 제외한 모든 전선으로 그래프 구성
        for j, wire in enumerate(wires):
            if i != j:  # i번째 전선은 끊어진 상태이므로 제외
                v1, v2 = wire
                # 무방향 그래프이므로 양쪽 모두에 연결 정보 추가
                graph[v1].append(v2)
                graph[v2].append(v1)
        
        # 방문 여부를 체크할 리스트. 송전탑 번호가 1부터 시작하므로 n+1 크기로 생성
        visited = [False] * (n + 1)
        
        # i번째 전선의 한쪽 송전탑에서 시작하여 연결된 모든 송전탑의 수를 계산
        count1 = dfs(graph, wires[i][0], visited)
        
        # 전체 송전탑 수에서 count1을 빼서 나머지 전력망의 송전탑 수를 계산
        count2 = n - count1
        
        # 두 전력망의 송전탑 수 차이 계산
        diff = abs(count1 - count2)
        
        # 최소 차이 갱신
        min_diff = min(min_diff, diff)

    # 모든 경우를 검사한 후, 가장 작은 차이 반환
    return min_diff

# DFS를 사용하여 연결된 송전탑의 수를 계산하는 함수
def dfs(graph, start, visited):
    # 현재 노드를 방문 처리
    visited[start] = True
    count = 1  # 현재 노드 포함
    
    # 현재 노드와 연결된 모든 미방문 노드에 대해 재귀적으로 DFS 수행
    for neighbor in graph[start]:
        if not visited[neighbor]:
            count += dfs(graph, neighbor, visited)
    
    # 연결된 모든 송전탑의 수 반환
    return count