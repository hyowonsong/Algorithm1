import java.util.*;

public class Solution {
    public int solution(int n) {
        int answer = 0;

        String str = Integer.toString(n);
        for (char c : str.toCharArray()) {
            // getNumericValue: char 형을 int 로 변환하는 메소드
            answer += Character.getNumericValue(c);
        }
        return answer;
    }
}