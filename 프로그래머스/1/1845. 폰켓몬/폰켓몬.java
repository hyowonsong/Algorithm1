import java.util.HashSet;

class Solution {
    public int solution(int[] nums) {
        // 선택할 수 있는 폰켓몬의 최대 수
        int maxSelection = nums.length / 2;

        // 폰켓몬의 중복을 제거하기 위해 HashSet 사용
        HashSet<Integer> Pokemons = new HashSet<>();

        // 폰켓몬 종류를 HashSet에 추가 (중복은 자동으로 제거됨)
        for (int num : nums) {
            Pokemons.add(num);
        }

        // 선택할 수 있는 폰켓몬의 종류 수는 maxSelection 과 uniquePokemons 크기 중 작은 값
        return Math.min(Pokemons.size(), maxSelection);
    }
}