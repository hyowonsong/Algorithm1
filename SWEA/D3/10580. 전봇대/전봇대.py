T = int(input())

for t in range(1, T + 1):
    N = int(input())  # 전선의 개수
    lines = []

    # 각 전선의 끝점 입력
    for _ in range(N):
        A, B = map(int, input().split())
        lines.append((A, B))

    cross_count = 0

    # 전선의 모든 쌍 비교
    for i in range(N):
        for j in range(i + 1, N):
            A1, B1 = lines[i]
            A2, B2 = lines[j]

            # 교차 조건 확인
            if (A1 < A2 and B1 > B2) or (A1 > A2 and B1 < B2):
                cross_count += 1

    # 결과 출력
    print(f"#{t} {cross_count}")