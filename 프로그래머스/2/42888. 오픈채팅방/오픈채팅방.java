import java.util.HashMap;
import java.util.ArrayList;

class Solution {
    // solution 메서드: 채팅방 로그를 처리하여 최종 메시지를 반환
    public String[] solution(String[] record){
        // Enter/Leave 메시지를 저장할 해시맵 생성
        HashMap<String, String> msg = new HashMap<>();
        // Enter 와 Leave 명령에 대한 메시지 매핑
        msg.put("Enter", "님이 들어왔습니다.");
        msg.put("Leave", "님이 나갔습니다.");

        // uid 와 닉네임을 저장할 해시맵 생성
        HashMap<String, String> uid = new HashMap<>();

        // record 배열의 각 요소를 순회하며 닉네임을 갱신
        for (String s : record) {
            // 각 명령어를 공백 기준으로 분리
            String[] cmd = s.split(" ");
            // Enter 또는 Change 명령어에 대해 닉네임 갱신
            // Enter 랑 Change 가 있으면 cmd 의 length 가 3이다. if 문 사용
            if (cmd.length == 3) {
                uid.put(cmd[1], cmd[2]);
            }
        }

        // 답을 저장할 answer 리스트 생성
        ArrayList<String> answer = new ArrayList<>();

        // record 배열을 다시 순회하며 메시지를 처리
        for (String s:record){
            // 각 명령어를 공백 기준으로 분리
            String[] cmd = s.split(" ");
            // Enter 또는 Leave 명령어인 경우 메시지 생성
            if(msg.containsKey(cmd[0])){
                // 유저 ID에 해당하는 닉네임과 메시지를 리스트에 추가
                answer.add(uid.get(cmd[1]) + msg.get(cmd[0]));
            }
        }

        // 최종 메시지를 String 배열로 변환하여 반환
        return answer.toArray(new String[0]);
    }
}