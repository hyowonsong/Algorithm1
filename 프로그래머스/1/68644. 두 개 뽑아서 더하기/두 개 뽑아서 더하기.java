import java.util.HashSet;

class Solution {
    public int[] solution(int[] numbers){
        // 1. 중복값 제거를 위해 해시셋 선택 - 어차피 나중에 sorted()로 순서 다시 정리해야
        // HashSet vs LinkedHashSet vs TreeSet
        // HashSet 은 평균적으로 O(1). 데이터의 유일성만 중요, 순서가 중요X
        // LinkedHashSet 은 평균적으로 O(1). 데이터 유일성 + 순서 유지
        // TreeSet 은 평균적으로  O(logN). 데이터 순서 유지 + 집합 특성 유지할 때
        HashSet<Integer> set = new HashSet<>();

        // 두 수를 더한 결과를 해시셋에 추가
        for (int i=0; i<numbers.length-1; i++){
            for (int j = i+1; j < numbers.length; j++){
                set.add(numbers[i] + numbers[j]);
            }
        }

        // 해시셋의 값을 오름차순 정렬하고 int[] 형태의 배열로 변환하여 반환
        // mapToInt() 는 각 Integer 객체를 기본형 int 로 변환하는 함수입니다.
        // Integer::intValue 는 Integer 객체의 intValue()메서드를 참조하여 int 값 얻습니다.
        // toArray() 는 IntStream 의 모든 요소를 int[] 배열로 변환합니다. 
        // toArray() 메서드는 스트림의 요소를 배열로 변환하는데 사용합니다. 
        return set.stream().sorted().mapToInt(Integer::intValue).toArray();
    }
}