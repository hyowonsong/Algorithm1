
import java.util.ArrayList;

// 가장 큰 수
public class Solution {
    // 각 숫자를 앞뒤로 붙여보고 큰 경우를 반환
    public String solution(int[] numbers){
        // int 형 정수 배열을 문자열로 바꾸어 list 에 저장
        ArrayList<String> list = new ArrayList<>();
        for (int number : numbers) {
            list.add(String.valueOf(number));
        }

        // 조합하여 비교하여 더 큰 수를 기준으로 내림차순 정렬합니다.
        list.sort((o1, o2) -> {
            int a = Integer.parseInt(o1 + o2);
            int b = Integer.parseInt(o2 + o1);
            return Integer.compare(b, a);
        });

        // 정렬된 수를 나열하여 문자열로 만듭니다.
        StringBuilder sb = new StringBuilder();
        for (String s : list) {
            sb.append(s);
        }

        // 문자열을 반환합니다. 맨앞에 "0" 이 있는 경우는 "0"만 반환합니다.
        return sb.charAt(0) == '0' ? "0" : sb.toString();
    }
}
