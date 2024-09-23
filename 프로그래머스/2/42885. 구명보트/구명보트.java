import java.util.Arrays;

class Solution {
    // 구명보트를 최대한 적게 사용해 모든 사람을 구출
    public int solution(int[] people, int limit){
        // 몸무게를 오름차순으로 정렬
        Arrays.sort(people);
        // 필요한 보트 개수
        int count = 0;
        // 가장 가벼운 사람을 가리키는 인덱스
        int i = 0;
        // 가장 무거운 사람을 가르키는 인덱스
        int j = people.length -1;
        
        while (i<=j){
            // 가장 무거운 사람과 가장 가벼운 사람을 같이 태울 수 있으면 두 사람 모두 보트에 태움
            if (people[i] + people[j] <= limit){
                i += 1;
            }
            // 무거운 사람만 태울 수 있으면 무거운 사람만 보트에 태움
            j -= 1; 
            count += 1;
        }
        return count;
    }
}