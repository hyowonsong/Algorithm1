# 퇴사

# N+1일째 되는 날 퇴사를 하기 위해 남은 N일동안 최대한 많은 상담
# 각각의 상담은 걸리는 시간 Ti, 받을 수 있는 금액 Pi

N = int(input())  
schedule = [list(map(int, input().split())) for _ in range(N)]

# DP 배열 초기화 
dp = [0] * (N + 1)

# 뒤에서부터 거꾸로 계산
for i in range(N - 1, -1, -1):
    T, P = schedule[i]  # i번째 날의 상담 소요 기간 T와 수익 P
    if i + T <= N:  # 상담을 할 수 있는 경우 (퇴사 이전에 상담 완료)
        # 상담을 선택한 경우와 선택하지 않은 경우 중 더 큰 이익 선택
        dp[i] = max(P + dp[i + T], dp[i + 1])
    else:
        # 상담을 할 수 없는 경우 (퇴사 이후 상담이 끝나는 경우)
        dp[i] = dp[i + 1]

# 첫째 날부터의 최대 이익 출력
print(dp[0])
