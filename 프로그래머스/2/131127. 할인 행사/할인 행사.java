import java.util.HashMap;

public class Solution {
    public int solution(String[] want, int[] number, String[] discount) {
        // want, number 배열의 값을 해시맵에 저장
        HashMap<String, Integer> wantMap = new HashMap<>();
        for (int i = 0; i < want.length; i++) {
            wantMap.put(want[i], number[i]);
        }

        // 총 일수를 계산할 변수 초기화
        int answer = 0;

        // 특정일 i에 회원가입 시 할인받을 수 있는 품목 체크
        for (int i = 0; i <= discount.length - 10; i++) { // i는 0부터 시작하여 discount.length - 10까지
            // i일 회원가입 시 할인받는 제품 및 개수를 담을 해시맵
            HashMap<String, Integer> discount10d = new HashMap<>();

            // i일 회원가입 시 할인받는 제품 및 개수로 해시맵 구성
            for (int j = i; j < i + 10; j++) { // j는 i부터 i + 10까지 순회
                if (j < discount.length) { // 인덱스가 범위를 넘어가지 않도록 확인
                    discount10d.put(discount[j], discount10d.getOrDefault(discount[j], 0) + 1);
                }
            }

            // 할인하는 상품의 개수가 원하는 수량과 일치하면 정답 변수에 1 추가
            if (discount10d.equals(wantMap)) {
                answer++;
            }
        }

        return answer;
    }
}
