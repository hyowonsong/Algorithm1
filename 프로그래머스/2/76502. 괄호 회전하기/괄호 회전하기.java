import java.util.ArrayDeque;

class Solution {
    // 주어진 문자열이 올바른 괄호 문자열인지 확인하는 함수
    public static boolean isValid(String s) {
        ArrayDeque<Character> stack = new ArrayDeque<>();

        for (char c : s.toCharArray()) {
            if (c == '(' || c == '[' || c == '{') {
                stack.push(c);  // 열린 괄호는 스택에 넣음
            } else {
                // 닫힌 괄호인데 스택이 비었거나 짝이 맞지 않으면 false
                if (stack.isEmpty()) return false;
                char openBracket = stack.pop();
                
                if (c == ')' && openBracket != '(') return false;
                if (c == ']' && openBracket != '[') return false;
                if (c == '}' && openBracket != '{') return false;
            }
        }

        // 모든 열린 괄호가 닫혔는지 확인
        return stack.isEmpty();
    }

    // 문자열을 왼쪽으로 한 칸 회전시키는 함수
    public static String rotate(String s) {
        // 문자열 s에서 인덱스 1부터 끝까지 문자열을 반환합니다.
        // s = "abcde" 라면 s.substring(1) 은 "bcde" 를 반환합니다.
        // s.charAt(0) 은 문자열 s의 인덱스 0, 즉, 첫번째 문자를 반환
        // 결합 : s.substring 과 s.charAt(0)에서 얻은 a 결합
        // bcdea 가 된다.
        return s.substring(1) + s.charAt(0);
    }

    public static int solution(String s) {
        int validCount = 0;
        String rotated = s;

        // 주어진 문자열의 길이만큼 회전시킴
        for (int i = 0; i < s.length(); i++) {
            if (isValid(rotated)) {
                validCount++;
            }
            rotated = rotate(rotated);  // 문자열을 한 칸 회전시킴
        }
        return validCount;
    }
}