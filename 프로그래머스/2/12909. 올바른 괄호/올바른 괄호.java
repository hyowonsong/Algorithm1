import java.util.ArrayDeque;

class Solution {
    boolean solution(String s) {
        // ArrayDeque 객체를 생성하여 stack 변수에 할당
        // Deque 에는 크게 ArrayDeque 와 LinkedList 가 존재.
        ArrayDeque<Character> stack = new ArrayDeque<>();

        for (char c : s.toCharArray()) {
            if (c == '(') {
                // 열린 괄호는 스택에 넣음
                stack.push(c);
            } else if (c == ')') {
                // 닫힌 괄호는 스택에서 열린 괄호를 꺼냄
                if (stack.isEmpty() || stack.pop() != '(') {
                    return false; // 스택이 비었거나 짝이 맞지 않으면 false
                }
            }
        }
        // 모든 괄호가 짝지어졌으면 스택이 비어 있어야 함
        return stack.isEmpty();
    }
}