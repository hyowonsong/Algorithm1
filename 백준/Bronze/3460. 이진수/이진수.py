T = int(input())

for i in range(T):
    n = int(input())
    positions = []
    position = 0

    while n>0:
        if n & 1:
            positions.append(position)
        n >>= 1
        position += 1

    print(' '.join(map(str,positions)))
