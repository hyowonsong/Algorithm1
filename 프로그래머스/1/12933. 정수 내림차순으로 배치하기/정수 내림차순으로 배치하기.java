import java.util.Arrays;
import java.util.Collections;

class Solution {
    public long solution(long n){
        // 정수 n 을 문자열로 변환하고 각 자릿수를 배열로 저장
        String[] digits = String.valueOf(n).split("");

        // 내림차순으로 정렬
        Arrays.sort(digits, Collections.reverseOrder());

        // 정렬된 숫자를 다시 하나의 문자열로 합칩
        StringBuilder sb = new StringBuilder();
        for (String digit: digits){
            sb.append(digit);
        }

        // 문자열을 long 으로 변환하여 반환
        // 문자열을 Long.parseLong() 메서드를 이용하여 long 형으로 변환하여 반환
        return Long.parseLong(sb.toString());
    }
}