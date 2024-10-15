from itertools import combinations

N, M = map(int, input().split())

# 1부터 N까지의 자연수 중에서 M개의 조합을 생성
combs = combinations(range(1, N + 1), M)

# 조합 결과를 출력
for comb in combs:
    print(' '.join(map(str, comb)))