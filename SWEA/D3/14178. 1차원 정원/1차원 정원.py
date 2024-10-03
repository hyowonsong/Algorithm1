T = int(input())  

for t in range(1, T + 1):
    N, D = map(int, input().split())  # N: 꽃의 수, D: 분무기의 범위
    cnt = 0  # 필요한 분무기 수
    pos = 1  # 현재 꽃의 위치

    while pos <= N:
        cnt += 1  # 분무기 추가
        pos += D * 2 + 1  # 다음 분무기를 놓을 위치 (현재 위치 + 범위의 끝)

    print(f"#{t} {cnt}") 