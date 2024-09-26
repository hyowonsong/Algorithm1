import java.util.HashSet;

class Solution {
    public int solution(int[] nums) {
        // 선택할 수 있는 폰켓몬의 최대 수
        int max = nums.length / 2;

        // 폰켓몬의 중복을 제거하기 위해 HashSet 사용
        HashSet<Integer> set = new HashSet<>();

        // 폰켓몬 종류를 HashSet에 추가 (중복은 자동으로 제거됨)
        // add : Set 에 요소를 추가할 때 사용되며, 중복된 요소는 추가X
        // put : Map 에 키와 값을 추가하거나 업데이트 할 때 사용
        for (int num : nums) {
            set.add(num);
        }

        // 폰켓몬의 종류 수는 max 과 set 크기 중 작은 값
        // set 크기는 size() 로 표시
        return Math.min(set.size(), max);
    }
}