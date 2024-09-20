import java.util.HashMap;
import java.util.HashSet;

class Solution {
    public int solution(int[] topping){
        // 결과값을 저장할 변수 초기화
        int answer = 0;

        // 토핑의 개수를 세어서 해시맵에 저장
        HashMap<Integer, Integer> toppingMap = new HashMap<>();
        for (int t: topping){
            toppingMap.put(t, toppingMap.getOrDefault(t,0) + 1);
        }
        
        // 토핑의 종류를 저장할 해시셋
        HashSet<Integer> toppingSet = new HashSet<>();
        
        // 롤케이크를 하나씩 해시셋에 넣으면서 확인
        for(int t: topping) {
            toppingSet.add(t);
            toppingMap.put(t, toppingMap.get(t) - 1);

            // 토핑의 전체 개수가 0이면 해시맵에서 제거
            if (toppingMap.get(t) == 0)
                toppingMap.remove(t);

            // 토핑의 종류의 수가 같다면
            if (toppingSet.size() == toppingMap.size())
                answer++;
        }
        
        // 공평하게 나눌 수 있는 방법의 수 반환
        return answer;
    }
}