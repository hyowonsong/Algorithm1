import java.util.ArrayDeque;

class Solution {
    public static int[] solution(int[] prices) {
        int n = prices.length;
        int[] answer = new int[n];
        ArrayDeque<Integer> stack = new ArrayDeque<>();

        for (int i = 0; i < n; i++) {
            // 스택이 비어있지 않고, 현재 가격이 스택의 맨 위 가격보다 작을 때
            while (!stack.isEmpty() && prices[stack.peekLast()] > prices[i]) {
                // 스택의 맨 위 가격 인덱스를 꺼내서
                int top = stack.pollLast();
                // 현재 인덱스 i에서 스택의 맨 위 가격 인덱스 top을 빼면 가격이 떨어지지 않은 기간이 됨
                answer[top] = i - top;
            }
            // 현재 가격의 인덱스를 스택에 추가
            stack.offerLast(i);
        }

        // 마지막 가격은 가격이 떨어지지 않은 기간이 없으므로 0으로 설정
        while (!stack.isEmpty()) {
            int top = stack.pollLast();
            answer[top] = n - 1 - top;
        }

        return answer;
    }
}