# N과 M(3)

from itertools import product

N, M = map(int, input().split())

# 중복 허용 조합을 생성
combinations = product(range(1, N + 1), repeat=M)

# 조합 결과를 출력
for comb in combinations:
    print(' '.join(map(str, comb)))
