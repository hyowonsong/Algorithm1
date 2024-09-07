public class Solution {
    boolean solution(String s) {
        boolean answer = true;

        s = s.toLowerCase();

        int pCount = 0;
        int yCount = 0;

        // 문자열을 하나씩 순회하며 'p'와 'y'의 개수를 센다.
        for (int i = 0; i < s.length(); i++) {
            char ch = s.charAt(i);
            if (ch == 'p') {
                pCount++;
            } else if (ch == 'y') {
                yCount++;
            }
        }

        // 'p'와 'y'의 개수가 같으면 true, 다르면 false 반환
        return pCount == yCount;
    }
}