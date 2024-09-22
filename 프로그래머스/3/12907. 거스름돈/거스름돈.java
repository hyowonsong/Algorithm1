class Solution {
    public int solution(int n, int[] money) {
        // dp[i]는 i원을 거슬러 줄 수 있는 경우의 수를 저장
        int[] dp = new int[n + 1];
        dp[0] = 1; // 0원을 거슬러 주는 방법은 1가지 (아무 동전도 사용하지 않음)

        // 각 동전 단위에 대해 경우의 수를 계산
        for (int coin : money) {
            for (int i = coin; i <= n; i++) {
                dp[i] = (dp[i] + dp[i - coin]) % 1000000007;
            }
        }

        // n원을 거슬러 줄 수 있는 경우의 수 반환
        return dp[n];
    }
}