# 모든 순열

from itertools import permutations

N = int(input())

perms = permutations(range(1,N+1))

for perm in perms:
    print(' '.join(map(str, perm)))
