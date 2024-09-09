import java.util.ArrayDeque;

class Solution {
    public static int solution(String s) {
        ArrayDeque<Character> stack = new ArrayDeque<>();

        // 문자열 s를 순차적으로 순회하면서 짝을 확인
        for (int i = 0; i < s.length(); i++) {
            char currentChar = s.charAt(i);

            // 스택이 비어 있으면 현재 문자를 스택에 추가
            if (stack.isEmpty()) {
                stack.push(currentChar);
            }
            // 스택의 마지막 문자와 현재 문자가 같으면 스택에서 제거
            else if (stack.peek() == currentChar) {
                stack.pop();
            }
            // 같지 않으면 현재 문자를 스택에 추가
            else {
                stack.push(currentChar);
            }
        }

        // 스택이 비어 있으면 모든 짝이 제거된 것이므로 1 반환
        if (stack.isEmpty()) {
            return 1;  // 스택이 비어 있으면 1을 반환
        } else {
            return 0;  // 스택이 비어 있지 않으면 0을 반환
        }
    }
}