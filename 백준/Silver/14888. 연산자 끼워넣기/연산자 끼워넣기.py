# 백트래킹 

N = int(input())
num = list(map(int, input().split()))
op = list(map(int, input().split()))  # +, -, *, //

# 수식을 계산하면서 maximum이 갱신될 때 무조건 현재 계산된 값이 더 크도록 하기 위함
maximum = -1e9
# 수식을 계산하면서 minimum이 갱신될 때 무조건 현재 계산된 값이 더 작도록 하기 위함
minimum = 1e9


def dfs(depth, total, plus, minus, multiply, divide):
    # global을 사용함으로써 함수 내에서 maximum, minimum은 전역변수
    global maximum, minimum
    if depth == N:
        maximum = max(total, maximum)
        minimum = min(total, minimum)
        return

    if plus:
        dfs(depth + 1, total + num[depth], plus - 1, minus, multiply, divide)
    if minus:
        dfs(depth + 1, total - num[depth], plus, minus - 1, multiply, divide)
    if multiply:
        dfs(depth + 1, total * num[depth], plus, minus, multiply - 1, divide)
    if divide:
        dfs(depth + 1, int(total / num[depth]), plus, minus, multiply, divide - 1)


dfs(1, num[0], op[0], op[1], op[2], op[3])
print(maximum)
print(minimum)