import java.util.HashMap;

class Solution {
    public String solution(String[] participant, String[] completion) {
        // 해시맵 생성
        HashMap<String, Integer> hashMap = new HashMap();
        // 완전한 선수들의 이름을 해시맵에 저장
        for (String string : completion) {
            hashMap.put(string, hashMap.getOrDefault(string, 0) + 1);
        }

        // 참가한 선수들의 이름을 키로 하는 값을 1씩 감소
        for (String string : participant) {
            if (hashMap.getOrDefault(string, 0) == 0) {
                return string;
            }
            hashMap.put(string, hashMap.get(string) - 1);
        }
        return null;
    }
}