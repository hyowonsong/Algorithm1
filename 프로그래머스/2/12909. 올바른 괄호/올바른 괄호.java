import java.util.ArrayDeque;

class Solution {
    boolean solution(String s) {
        // ArrayDeque 객체를 생성하여 stack 변수에 할당
        // Deque 에는 크게 ArrayDeque 와 LinkedList 가 존재.
        ArrayDeque<Character> stack = new ArrayDeque<>();

        for (char c : s.toCharArray()) {
            // 여는 괄호 '('는 스택에 추가
            if (c == '(') {
                stack.push(c);
            } else {
                // 닫는 괄호 ')'일 때 스택이 비어있거나, 짝이 맞지 않으면 false 반환
                if (stack.isEmpty() || stack.pop() != '(') {
                    return false;
                }
            }
        }
        // 모든 괄호가 짝지어졌으면 스택이 비어 있어야 함
        // 모든 열린 괄호가 짝이 맞춰지면 true 그렇지 않으면 false
        return stack.isEmpty();
    }
}