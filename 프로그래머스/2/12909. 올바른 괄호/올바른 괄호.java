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
                //스택이 비어있거나 스택을 빼내었을 때 ( 가 아니라면 false 반환
                if (stack.isEmpty() || stack.pop() != '(') {
                    return false; 
                }
            }
        }
        // 모든 괄호가 짝지어졌으면 스택이 비어 있어야 함
        return stack.isEmpty();
    }
}