import java.util.HashSet;

class Solution {
    public int[] solution(int[] numbers){
        // 1. 중복값 제거를 위해 해시셋 선택 - 어차피 나중에 sorted()로 순서 다시 정리해야
        // HashSet vs LinkedHashSet vs TreeSet
        // HashSet 은 평균적으로 O(1). 데이터의 유일성만 중요, 순서가 중요X
        // LinkedHashSet 은 평균적으로 O(1). 데이터 유일성 + 순서 유지
        // TreeSet 은 평균적으로  O(logN). 데이터 순서 유지 + 집합 특성 유지할 때
        HashSet<Integer> set = new HashSet<>();

        // 두 수를
        for (int i=0; i<numbers.length-1; i++){
            for (int j = i+1; j < numbers.length; j++){
                set.add(numbers[i] + numbers[j]);
            }
        }

        //
        return set.stream().sorted().mapToInt(Integer::intValue).toArray();
    }
}