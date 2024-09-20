import java.util.Arrays;
import java.util.HashSet;

class Solution {
    public int[] solution(String s) {
        // 입력 문자열 s에서 마지막 두 문자(}})를 제거하기 위해 전체 길이 -2
        // 문자열에서 { 를 제거하여 괄호 없는 숫자 목록만 남기도록
        s = s.substring(0, s.length() - 2).replace("{", "");
        // 문자열 s에서 대괄호를 제거하고 "},"을 기준으로 나누어 배열에 저장한 후 길이 기준으로 오름차순 정렬합니다.
        String[] arr = s.split("},");
        Arrays.sort(arr, (o1, o2) -> Integer.compare(o1.length(), o2.length()));

        // 중복을 제거하기 위해 HashSet을 생성
        HashSet<String> set = new HashSet<>();
        // 최종적으로 반환할 배열 answer를 생성합니다.
        // 배열의 크기는 튜플의 개수(arr.length)와 동일
        int[] answer = new int[arr.length];

        // 각 원소를 순회하면서 이전 원소와 차이 나는 부분을 구합니다.
        for (int i = 0; i < arr.length; i++) {
            // 현재 순회 중인 튜플을 쉼표(,)를 기준으로 나누어 문자열 배열 numbers에 저장
            String[] numbers = arr[i].split(",");
            for (String number : numbers) {
                // set에 현재 숫자가 포함되지 않았는지 확인
                if (!set.contains(number)) {
                    // 중복이 아니라면 현재 숫자를 정수로 변환하여 answer 배열의 i번째 위치에 저장
                    answer[i] = Integer.parseInt(number);
                    // 처리한 숫자를 set에 추가하여 이후에 중복으로 처리되지 않도록
                    set.add(number);
                }
            }
        }
        return answer;
    }
}