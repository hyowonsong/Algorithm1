T = int(input())

for t in range(1, T + 1):
    N = int(input())
    # 노선의 범위를 저장할 리스트
    bus_routes = []

    # 각 노선의 범위 입력
    for i in range(N):
        A, B = map(int, input().split())
        bus_routes.append((A, B))

    # 버스 정류장 수 입력
    P = int(input())
    results = []

    # 각 버스 정류장에 대해 노선 개수 세기
    for i in range(P):
        bus_number = int(input())
        count = 0

        # 각 노선의 범위와 비교하여 노선 개수 카운트
        for A, B in bus_routes:
            if A <= bus_number <= B:
                count += 1
        
        # 결과 리스트에 저장
        results.append(count)

    # 결과 출력
    print(f"#{t}", " ".join(map(str, results)))