current_sum = 0
max_sum = 0

for i in range(10):
    out, in_ = map(int,input().split())

    current_sum = current_sum + in_ - out

    if current_sum > max_sum:
        max_sum = current_sum

print(max_sum)