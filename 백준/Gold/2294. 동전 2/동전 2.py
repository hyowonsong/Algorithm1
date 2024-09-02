# 동전 2
# 동전의 합이 k 원 + 동전의 개수가 최소

n, k = map(int, input().split())

coins = []
for _ in range(n):
    coins.append(int(input()))

# DP 테이블 초기화
dp = [float('inf')] * (k + 1)  # 무한대로 초기화
dp[0] = 0  # 0원을 만드는 데 필요한 동전의 개수는 0개

# DP 테이블 갱신
for coin in coins:
    for i in range(coin, k + 1):
        dp[i] = min(dp[i], dp[i - coin] + 1)

# 결과 출력
if dp[k] != float('inf'):
    print(dp[k])
else:
    print(-1)