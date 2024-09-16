import java.util.Arrays;

class Solution {
    public static String[] solution(String[] strings, int n) {
        // 문자열 배열을 정렬합니다.
        // Arrays.sort 메소드에 Comparator 를 사용하여 사용자 정의 정렬 기준을 적용합니다.
        Arrays.sort(strings, (s1, s2) -> {
            // 인덱스 n의 문자를 각각 추출합니다.
            char c1 = s1.charAt(n);  // 문자열 s1의 인덱스 n의 문자
            char c2 = s2.charAt(n);  // 문자열 s2의 인덱스 n의 문자

            // 문자 비교: 인덱스 n의 문자를 기준으로 비교합니다.
            // Character.compare 메소드는 두 문자를 비교하여,
            // 음수, 양수, 0을 반환하여 정렬 순서를 결정합니다.
            if (c1 != c2) {
                // c1과 c2가 다르면, 두 문자의 사전 순서를 비교합니다.
                // Character.compare(c1, c2) 메소드는 c1이 c2보다 사전적으로 앞이면 음수를 반환하고,
                // c1이 c2보다 뒤면 양수를 반환합니다.
                return Character.compare(c1, c2);
            }

            // 인덱스 n의 문자가 같으면, 전체 문자열을 사전 순서로 비교합니다.
            // s1.compareTo(s2) 메소드는 두 문자열을 사전 순서로 비교합니다.
            // s1이 s2보다 앞이면 음수를 반환하고, s1이 s2보다 뒤면 양수를 반환합니다.
            // 둘이 같으면 0을 반환합니다.
            return s1.compareTo(s2);
        });

        // 정렬된 문자열 배열을 반환합니다.
        return strings;
    }
}