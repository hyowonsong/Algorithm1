T = int(input())

for t in range(1, T + 1):
    s = input().strip()
    pattern_length = 0

    for length in range(1, 11):
        pattern = s[:length]
        # 처음 두 번 반복되는 패턴 찾기
        if s[:length*2] == pattern * 2:
            pattern_length = length
            break

    print(f'#{t} {pattern_length}')