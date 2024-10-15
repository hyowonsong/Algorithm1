from itertools import permutations

N, M = map(int, input().split())

# 1부터 N까지의 숫자 중에서 M개의 숫자를 선택하여 순열 생성
perms = permutations(range(1, N+1), M)

for perm in perms:
    print(' '.join(map(str, perm)))