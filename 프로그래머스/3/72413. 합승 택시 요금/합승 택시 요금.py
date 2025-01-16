def solution(n, s, a, b, fares):
    INF = float('inf')
    # 그래프 초기화
    graph = [[INF] * (n + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        graph[i][i] = 0  # 자기 자신으로 가는 비용은 0
    
    for c, d, f in fares:
        graph[c][d] = f
        graph[d][c] = f
    
    # 플로이드-워셜 알고리즘
    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])
    
    # 최소 비용 계산
    min_cost = INF
    for t in range(1, n + 1):  # 경유 지점
        cost = graph[s][t] + graph[t][a] + graph[t][b]
        min_cost = min(min_cost, cost)
    
    return min_cost
