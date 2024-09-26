import java.util.HashMap;

public class Solution {
    public int solution(String[] want, int[] number, String[] discount) {
        // want, number 배열의 값을 해시맵에 저장
        // 고객이 원하는 제품과 그에 해당하는 수량을 저장하는 HashMap을 생성
        HashMap<String, Integer> wantMap = new HashMap<>();
        for (int i = 0; i < want.length; i++) {
            // 각 제품과 수량을 맵에 저장 (제품이 key, 수량이 value)
            wantMap.put(want[i], number[i]);
        }

        // 총 일수를 계산할 변수 초기화 (정답을 담을 변수)
        int answer = 0;

        // i일에 회원가입 시 할인받을 수 있는 품목 체크 (10일 간격으로 검사)
        // i는 0부터 시작하여 discount.length - 10까지 반복 (10일 단위로 확인)
        for (int i = 0; i <= discount.length - 10; i++) {
            // i일 회원가입 시 할인받는 제품 및 개수를 담을 해시맵 초기화
            HashMap<String, Integer> discount10d = new HashMap<>();

            // j는 i부터 시작해 i + 10일까지 순회 (10일 동안 확인)
            for (int j = i; j < i + 10; j++) {
                // 인덱스가 discount 배열의 범위를 넘어가지 않도록 확인
                if (j < discount.length) {

                    // 할인되는 제품을 해시맵에 저장하거나, 이미 있다면 수량을 증가
                    discount10d.put(discount[j], discount10d.getOrDefault(discount[j], 0) + 1);
                }
            }
            // 할인하는 상품의 개수가 원하는 수량과 일치하는지 비교
            // 두 해시맵 (wantMap과 discount10d)이 동일한지 확인
            if (discount10d.equals(wantMap)) {
                // 같다면 해당 기간에 구매 가능하므로 정답 카운트를 1 증가
                answer++;
            }
        }
        // 최종적으로 가능한 모든 기간을 확인 후, 그 결과 반환
        return answer;
    }
}
