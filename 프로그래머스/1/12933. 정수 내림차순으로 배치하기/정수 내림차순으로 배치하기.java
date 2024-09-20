import java.util.Arrays;
import java.util.Collections;

class Solution {
    // 입력을 보면 80억까지 들어올 수 있기 때문에 long 사용
    public long solution(long n){
        // 정수 n 을 문자열로 변환하고 각 자릿수를 배열로 저장
        // valueof 는 n 이 어떤 타입이든 문자열로 변환해줍니다.
        String[] digits = String.valueOf(n).split("");

        // 내림차순으로 정렬
        Arrays.sort(digits, Collections.reverseOrder());


        // 정렬된 숫자를 다시 하나의 문자열로 합칩
        StringBuilder sb = new StringBuilder();
        for (String digit : digits){
            sb.append(digit);
        }
        
        // 문자열을 Long.parseLong() 메서드를 이용하여 long 형으로 변환하여 반환
        // StringBuilder 에 저장된 숫자를 문자열로 변환 후, 그 문자열을 다시 long 타입 변환
        // StringBuilder 의 내용은 문자열로 표현되지만, 그 자체로는 문자열이 아닙니다.
        // 문자열을 더할 때 새로운 객체를 생성하는 것이 아니라 기존의 데이터에 더하는 방식이기 때문
        // int 는 4 바이트(32비트) long 은 64비트
        // int 타입의 숫자가 long 타입으로 변환된다면, 이 과정은 자동형변환
        // long 을 int 로 변환할 때는 명시적인 형 변환
        return Long.parseLong(sb.toString());
    }
}