import java.util.ArrayDeque;

class Solution {
    public int solution(String s) {
        // 같은 알파벳이 2개 붙어 있는 짝을 찾고 제거하는 문제

        // 문자들을 저장할 스택을 생성 (연결된 동일 문자를 처리하기 위함)
        ArrayDeque<Character> stack = new ArrayDeque<>();

        // 문자열의 모든 문자를 순서대로 확인
        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i); // 현재 위치의 문자를 가져옴

            // 스택이 비어있지 않고, 스택의 맨 위에 있는 문자와 현재 문자가 같으면
            if (!stack.isEmpty() && stack.peek() == c) {
                stack.pop(); // 스택에서 맨 위의 문자를 제거 (짝을 이루는 두 문자를 제거)
            } else {
                stack.push(c); // 짝이 없으면 현재 문자를 스택에 추가
            }
        }

        // 스택이 비어 있으면 모든 짝이 제거되었으므로 1을 반환, 그렇지 않으면 0 반환
        return stack.isEmpty() ? 1 : 0;
    }
}