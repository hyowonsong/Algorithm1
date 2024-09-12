// 다단계 칫솔 판매
import java.util.HashMap;

// 판매원이 칫솔을 판매하면 그 이익이 조금씩 분배되는 형태의 판매망
// 모든 판매원은 칫솔의 판매에 의하여 발생하는 이익을 계산하여 배분하고 가진다.
// 모든 판매원은 칫솔의 판매에 의하여 발생하는 이익에서 10% 계산하여 자신을
// 조직에 참여시킨 추천인에게 배분하고 나머지는 자신이 가진다.
// 모든 판매원은 자신이 조직에 추천하여 가입시킨 판매원에게서 발생하는 이익의 10%까지 자신에 이익
// 10%를 계산할 때는 1원 미만인 경우에는 이득을 분배하지 않고 자신이 모두 가진다.

// N은 enroll의 길이, M 은 seller의 길이로 seller 별로 enroll을 탐색하므로
// 시간 복잡도는 O(N*M)

public class Solution {
    // 판매자의 관계에 부모-자식 관계가 존재(트리)
    // 부모 노드가 자신을 추천한 판매원
    // enroll 을 키, referral 을 값으로 놔두기
    public int[] solution(String[] enroll, String[] referral, String[] seller, int[] amount){
        // parent 해시맵, key 는 enroll 의 노드, value 는 referral 의 노드
        HashMap<String, String> parent = new HashMap<>();
        for (int i=0; i<enroll.length; i++){
            parent.put(enroll[i], referral[i]);
        }

        // total 해시맵 생성
        HashMap<String, Integer> total = new HashMap<>();

        // seller 배열과 amount 배열을 이용하여 이익 분배
        for (int i = 0; i < seller.length; i++) {
            String curName = seller[i];
            // 판매자가 판매한 총 금액 계산
            int money = amount[i] * 100;
            // 판매자부터 차례대로 상위 노드로 이동하며 이익 분배
            // 분배할 금액이 남아 있고 curName 이 "-" 아니라면
            while (money > 0 && !curName.equals("-")) {
                // 현재 판매자가 받을 금액 계산(10%를 제외한 금액)
                total.put(curName, total.getOrDefault(curName, 0) + money - (money / 10));
                // 현재 판매자의 상위 추천인을 parent에서 찾아서 curName을 갱신
                curName = parent.get(curName);
                // 현재 분배할 금액을 10%로 줄입니다
                money /= 10;
            }
        }

        // enroll 배열의 모든 노드에 대해 해당하는 이익을 배열로 반환
        int[] answer = new int[enroll.length];
        // enroll[i]에 해당하는 판매원의 최종 이익을 total 맵에서 찾아 answer 배열에 저장
        for (int i = 0; i < enroll.length; i++) {
            // getOrDefault는 해당 판매원이 이익을 얻지 않았다면 0을 반환
            answer[i] = total.getOrDefault(enroll[i], 0);
        }
        return answer;
    }
}