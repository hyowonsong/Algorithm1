# 2진 트리 모양 초원의 루트 노드에서 출발하여 각 노드를 돌아다니며 양을 모은다.
# 각 노드를 방문할 때마다 해당 노드에 있던 양과 늑대가 따라온다.
# 이때, 내가 모은 양의 수보다 늑대의 수가 같거나 더 많으면 모든 양을 잡아먹는다.
# 양이 늑대에게 잡아먹히지 않도록 하면서 최대한 많은 수의 양을 모아서 다시 루트 노드로 돌아오려 한다.

# 각 노드에 있는 양 또는 늑대에 대한 정보가 담긴 배열 info
# 2진 트리의 각 노드들의 연결 관계를 담은 2차원 배열 edges가 매개변수로 주어질 때,
# 문제에 제시된 조건에 따라 각 노드를 방문하면서 모을 수 있는 양은 최대 몇 마리인지 return

def dfs(current_state, sheep, wolf, info, edges):
    if sheep <= wolf:  # 늑대가 양보다 많거나 같으면 불가능한 상태
        return 0
    
    max_sheep = sheep  # 현재까지의 최대 양의 수
    
    # 현재 방문할 수 있는 모든 노드들의 집합을 계산
    next_possible = set()
    for parent, child in edges:
        if parent in current_state:  # 부모 노드를 방문했다면
            next_possible.add(child)  # 자식 노드를 방문 가능한 노드로 추가
    next_possible -= current_state  # 이미 방문한 노드 제외
    
    # 각각의 다음 노드에 대해 방문을 시도
    for next_node in next_possible:
        next_state = current_state.copy()  # 현재 상태를 복사
        next_state.add(next_node)  # 다음 노드를 복사된 집합에 추가
        
        # 다음 노드가 양인 경우
        if info[next_node] == 0:
            max_sheep = max(max_sheep, 
                          dfs(next_state, sheep + 1, wolf, info, edges))
        # 다음 노드가 늑대인 경우
        else:
            max_sheep = max(max_sheep, 
                          dfs(next_state, sheep, wolf + 1, info, edges))
    
    return max_sheep

def solution(info, edges):
    # 루트 노드는 항상 양이므로 sheep=1로 시작
    return dfs({0}, 1, 0, info, edges)
