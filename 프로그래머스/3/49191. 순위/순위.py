def solution(n, results):
    # 그래프 초기화
    graph = [[0] * (n + 1) for _ in range(n + 1)]

    # 주어진 경기 결과를 그래프에 반영(results의 각 [win, lose] 읽기)
    for win, lose in results:  
        graph[win][lose] = 1  # win 선수가 lose 선수를 이김
        graph[lose][win] = -1  # lose 선수가 win 선수에게 짐

    # 플로이드-워셜 알고리즘으로 간접적인 승패 관계 계산
    for k in range(1, n + 1):  # k: 중간 선수 (경유지)
        for i in range(1, n + 1):  # i: 출발 선수
            for j in range(1, n + 1):  # j: 도착 선수
                # i 선수가 k 선수를 이기고, k 선수가 j 선수를 이긴 경우
                if graph[i][k] == 1 and graph[k][j] == 1:
                    graph[i][j] = 1  # i 선수가 j 선수를 이김
                # i 선수가 k 선수에게 지고, k 선수가 j 선수에게 진 경우
                elif graph[i][k] == -1 and graph[k][j] == -1:
                    graph[i][j] = -1  # i 선수가 j 선수에게 짐

    # 정확히 순위를 매길 수 있는 선수의 수 계산
    answer = 0 
    for i in range(1, n + 1): 
        count = 0  # 명확한 승패 관계의 수를 세기 위한 변수 초기화
        for j in range(1, n + 1):  # 다른 모든 선수와의 관계 확인
            if graph[i][j] != 0:  # graph[i][j]가 0이 아니면 승패 관계가 명확함
                count += 1  # 명확한 관계 수 증가
                
        # 다른 모든 선수(n-1명)와의 승패 관계가 명확한 경우
        if count == n - 1:  
            answer += 1  # 순위를 매길 수 있는 선수로 카운트

    return answer  # 순위를 매길 수 있는 선수의 수 반환
