T = int(input())

for i in range(1, T + 1):
    total_sum = 0
    n = list(map(int, input().split()))

    for num in n:
        if num % 2 == 1:
            total_sum += num

    print(f'#{i} {total_sum}')
