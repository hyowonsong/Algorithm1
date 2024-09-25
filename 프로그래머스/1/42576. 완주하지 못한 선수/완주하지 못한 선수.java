import java.util.HashMap;

class Solution {
    public String solution(String[] participant, String[] completion) {
        // 해시맵 생성
        HashMap<String, Integer> hashMap = new HashMap<>();

        // 참가자가 아닌 완주자들의 이름을 해시맵에 저장
        for (String string : completion){
            // getOrDefault(string,0) : hashMap 에서 키가 string 인 것을 가져옵니다.
            // 만약 string 이라는 키가 존재한다면 그 키에 대응
            // 만약 string 이라는 키가 존재하지 않으면 기본값으로 0 을 반환
            hashMap.put(string, hashMap.getOrDefault(string,0)+1);
        }

        // 참가한 선수들의 이름을 키로 하는 값을 1씩 감소
        for (String string : participant){
            // 해당 선수 이름이 해시맵에 없거나(완주자 명단에 없는 경우), 이미 다 처리된 경우(카운트가 0인 경우)
            if (hashMap.getOrDefault(string, 0) == 0){
                // 완주하지 못한 선수이므로 그 선수 이름을 반환
                return string;
            }
            // 해당 선수 이름의 카운트를 1 감소 (즉, 이 선수를 처리함)
            hashMap.put(string, hashMap.get(string)-1);
        }
        // 모든 선수가 완주한 경우 null 을 반환
        return null;
    }
}