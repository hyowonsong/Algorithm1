import java.util.ArrayDeque;

class Solution {
    public static String solution(String[] cards1, String[] cards2, String[] goal) {
        // 카드 덱을 초기화합니다.
        ArrayDeque<String> deck1 = new ArrayDeque<>();
        ArrayDeque<String> deck2 = new ArrayDeque<>();

        // 주어진 카드 배열을 각각의 덱에 채웁니다.
        for (String card : cards1) {
            deck1.add(card);
        }
        for (String card : cards2) {
            deck2.add(card);
        }

        // 목표 배열을 처리합니다.
        for (String word : goal) {
            // 첫 번째 덱이 비어있지 않고, 목표 단어가 첫 번째 카드와 같으면
            if (!deck1.isEmpty() && word.equals(deck1.peek())) {
                deck1.poll(); // 첫 번째 카드를 제거합니다.
            }
            // 두 번째 덱이 비어있지 않고, 목표 단어가 첫 번째 카드와 같으면
            else if (!deck2.isEmpty() && word.equals(deck2.peek())) {
                deck2.poll(); // 두 번째 카드를 제거합니다.
            }
            // 목표 단어가 두 덱의 첫 번째 카드와도 일치하지 않는 경우
            else {
                return "No"; // 불가능하므로 "No"를 반환합니다.
            }
        }

        return "Yes"; // 모든 단어를 성공적으로 처리했으므로 "Yes"를 반환합니다.
    }
}
