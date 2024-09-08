import java.util.ArrayDeque;
import java.util.LinkedList;
import java.util.List;

class Solution {
    public static List<Integer> solution(int[] progresses, int[] speeds) {
        List<Integer> answer = new LinkedList<>();
        ArrayDeque<Integer> queue = new ArrayDeque<>();

        // 각 기능의 배포까지 걸리는 날 수를 계산하여 큐에 저장
        for (int i = 0; i < progresses.length; i++) {
            int remainingWork = 100 - progresses[i];
            int days = (remainingWork + speeds[i] - 1) / speeds[i];  // 올림 연산
            queue.add(days);
        }

        // 배포일 계산
        // 큐가 비어 있지 않을 때까지 계산
        while (!queue.isEmpty()) {
            int current = queue.poll();  // 현재 기능의 배포일
            int count = 1;


            //큐가 비어 있지 않고,큐의 첫 번째 요소가 현재 배포일 보다 작거나 같은 경우
            while (!queue.isEmpty() && queue.peek() <= current) {
                // 해당 요소를 제거
                queue.poll();
                count++;
            }
            answer.add(count);
        }
        return answer;
    }
}