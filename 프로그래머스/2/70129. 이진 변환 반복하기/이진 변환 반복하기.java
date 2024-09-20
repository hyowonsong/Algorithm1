// 이진 변환 반복하기
// 이진 변환의 횟수와 변환 과정에서 제거된 모든 0의 개수를 배열에 담아 반환
public class Solution {
    // 1. 처음에는 0과 1로 이루어진 문자열에서 0을 전부 없앤다.
    // 2. 0을 제거한 2진수의 길이를 다시 2진수로 표현합니다.
    // 3. 2에서 표현한 2진수가 1이 아니면 이진 변환 결과를 가지고 1부터 반복
    // 4. 이 것을 1이 될때까지 반복

    public int[] solution(String s){
        // 1. 이진 변환 횟수를 저장하는 변수
        int countTransform = 0;

        // 2. 제거된 모든 0의 개수를 저장하는 변수
        int countZero = 0;

        // 3. s가 '1'이 아닌 동안 계속 반복
        while (!s.equals("1")) {
            // 4. 이진 변환 횟수를 1 증가
            countTransform++;

            // 문자열에서 '1'을 제거하고 남은 문자의 개수, 즉 '0'의 개수를 계산
            // s에서 '0' 의 개수를 세어 countZero 에 누적
            int zero = s.replace("1", "").length();
            countZero += zero;

            // s에서 '1'의 개수를 세고, 이를 이진수로 변환
            // Integer.toBinaryString() 메서드를 사용
            s = Integer.toBinaryString(s.length() - zero);
        }

        // 이진 변환 횟수와 제거된 모든 '0'의 개수를 배열에 담아 반환
        return new int[]{countTransform, countZero};
    }
}
