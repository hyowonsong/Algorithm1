// 2*n 타일링
// 반드시 1번부터 차례대로 구하면서 식을 찾아보자!!!!

class Solution {
    // 동적 계획법은 작은 반복이 계속 되어야 한다.

    // 타일을 채우는 마지막 경우만 고려하면 된다.
    // 가로로 타일을 놓는 경우 : 가로로 2개의 타일이 들어가야 n-2
    // 세로로 타일을 놓은 경우 : 타일 1개를 세로로 놓으므로 n-1 크기의
    // 직사각형을 채운 후 마지막에 가로로 2개를 놓는 것
    public int solution(int n){
        int[] dp = new int[n+1];
        // 세로만 구할 수 있는 경우 1개
        dp[1] = 1;
        // 가로만 구할 수 있는 경우 2개
        dp[2] = 2;
        
        for (int i =3; i<=n; i++){
            dp[i] = (dp[i-1]+dp[i-2])%1000000007;
        }
        return dp[n];
    }
}