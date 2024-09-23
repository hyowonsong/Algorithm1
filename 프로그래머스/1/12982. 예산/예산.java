import java.util.Arrays;

class Solution {
    // 배열 d와 예산 budget 이 주어질 때 최대 몇 개의 부서에 물품 지원?
    // 부서별로 신청한 금액을 오름차순으로 정렬한 후 맨 앞부터 순회하면서
    // 남은 예산이 신청한 금액보다 크면 예산 금액에서 차감

    public int solution(int[] d, int budget){
        Arrays.sort(d);
        int count = 0;

        for (int amount:d){
            if (amount > budget){
                break;
            }
            budget -= amount;
            count ++;
        }
        return budget >=0 ? count : count-1;
    }
}