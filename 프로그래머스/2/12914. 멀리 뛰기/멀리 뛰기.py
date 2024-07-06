# 멀리 뛰기
# 한번에 1칸 또는 2칸(dp 문제 같은데)

# n=1 ->1
# n=2 ->2
# n=3 ->3
# n=4 ->5
# n=5 ->8

def solution(n):
    if n<3:
        return n
    else:
        dp = [0] * (n+1)          # 반드시 DP 테이블 초기화 
        dp[1] = 1
        dp[2] = 2
        for i in range(3,n+1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n] % 1234567