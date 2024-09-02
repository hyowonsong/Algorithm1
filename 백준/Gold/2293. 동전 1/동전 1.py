n, k = map(int, input().split())

coins = []
for _ in range(n):
    coins.append(int(input()))

# 다이나믹 테이블을 생성하고 0번째 인덱스를 1로 지정
dp = [0] * (k + 1)
dp[0] = 1

# 코인 종류별로 다이나믹 테이블 순회
for coin in coins:
    for i in range(coin, k + 1):
        dp[i] += dp[i - coin]

print(dp[k])
