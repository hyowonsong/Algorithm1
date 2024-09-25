import java.util.ArrayDeque;
import java.util.Arrays;

// 카드 뭉치
public class Solution {
    public String solution(String[] cards1, String[] cards2, String[] goal) {
        // cards 와 goal 을 deque 로 변환
        ArrayDeque<String> cardsDeque1 = new ArrayDeque<>(Arrays.asList(cards1));
        ArrayDeque<String> cardsDeque2 = new ArrayDeque<>(Arrays.asList(cards2));
        ArrayDeque<String> goalDeque = new ArrayDeque<>(Arrays.asList(goal));

        // goalDeque 에 문자열이 남아 있으면 계속 반복
        while (!goalDeque.isEmpty()) {

            // cardsDeque1 의 front 와 일치하는 경우
            if (!cardsDeque1.isEmpty() && cardsDeque1.peekFirst().equals(goalDeque.peekFirst())) {
                cardsDeque1.pollFirst();
                goalDeque.pollFirst();
            }

            // cardsDeque2의 front 와 일치하는 경우
            else if (!cardsDeque2.isEmpty() && cardsDeque2.peekFirst().equals(goalDeque.peekFirst())) {
                cardsDeque2.pollFirst();
                goalDeque.pollFirst();
            } else {
                break; // 일치하는 원소를 찾지 못했으므로 종료
            }
        }
        // goal 이 비었으면 "Yes" 아니면 "No"를 반환
        return goalDeque.isEmpty() ? "Yes" : "No";
    }
}