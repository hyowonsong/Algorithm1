import java.util.HashMap;
import java.util.ArrayList;
import java.util.List;

public class Solution {
    public String[] solution(String[] record) {
        HashMap<String, String> userDict = new HashMap<>(); // 사용자 ID와 최종 닉네임을 저장할 맵
        List<String> actions = new ArrayList<>(); // 최종 메시지를 저장할 리스트

        // 첫 번째 순회: 사용자 ID와 최종 닉네임 매핑
        for (String r : record) {
            String[] parts = r.split(" "); // 각 레코드를 공백으로 분리
            String action = parts[0]; // 첫 번째 요소는 액션(Enter, Leave, Change)
            String userId = parts[1]; // 두 번째 요소는 사용자 ID

            // Enter나 Change 액션의 경우 닉네임 업데이트
            if (action.equals("Enter") || action.equals("Change")) {
                String nickname = parts[2]; // 세 번째 요소는 닉네임
                userDict.put(userId, nickname); // 사용자 ID와 닉네임 매핑 업데이트
            }
        }

        // 두 번째 순회: 최종 메시지 생성
        for (String r : record) {
            String[] parts = r.split(" "); // 각 레코드를 다시 공백으로 분리
            String action = parts[0]; // 액션 확인
            String userId = parts[1]; // 사용자 ID 확인

            // Enter 액션: 입장 메시지 생성
            if (action.equals("Enter")) {
                actions.add(userDict.get(userId) + "님이 들어왔습니다.");
            }
            // Leave 액션: 퇴장 메시지 생성
            else if (action.equals("Leave")) {
                actions.add(userDict.get(userId) + "님이 나갔습니다.");
            }
        }

        return actions.toArray(new String[0]); // 최종 메시지 리스트를 배열로 변환하여 반환
    }
}