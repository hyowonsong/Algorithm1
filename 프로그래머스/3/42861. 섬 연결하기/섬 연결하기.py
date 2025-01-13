
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

def solution(n, costs):
    # 비용순으로 정렬
    costs.sort(key=lambda x: x[2])
    
    # 부모 테이블 초기화
    parent = [i for i in range(n)]
    
    total_cost = 0
    bridge_count = 0
    
    # 모든 간선에 대해 처리
    for cost in costs:
        a, b, c = cost  # a, b는 섬 번호, c는 비용
        
        # 사이클이 발생하지 않는 경우에만 집합에 포함
        if find_parent(parent, a) != find_parent(parent, b):
            union_parent(parent, a, b)
            total_cost += c
            bridge_count += 1
            
        # 필요한 다리 개수는 n-1개
        if bridge_count == n-1:
            break
    
    return total_cost