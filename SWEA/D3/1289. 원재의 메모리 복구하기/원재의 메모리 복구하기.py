T = int(input())

for t in range(1, T + 1):
    n = list(input().strip())

    # 변경 횟수 초기화
    ans = 0

    # 1이 처음 등장하는 인덱스를 찾기
    if '1' in n:
        first = n.index('1')
        ans = 1  # 1이 나왔으므로 최소 1번의 변경이 필요함

        # 1이 나온 인덱스 이후부터 비교
        for i in range(first + 1, len(n)):
            if n[i - 1] != n[i]:
                ans += 1

    # 만약 1이 없다면 ans는 0으로 남아있음

    print(f"#{t} {ans}")
