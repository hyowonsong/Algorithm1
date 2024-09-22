class Solution {
    // 현재 10만 제한이 있기 때문에 재귀가 아니라 반드시 메모이제이션 사용
    public int solution(int n){
        int[] fibo = new int[n+1];
        fibo[0] = 0;
        fibo[1] = 1;

        for (int i = 2; i<=n; i++){
            fibo[i] = (fibo[i-1] + fibo[i-2]) % 1234567;
        }
        return fibo[n];
    }
}