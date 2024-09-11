// 1. 시간복잡도 : N은 words 의 길이.
// 2. words 의 길이만큼 반복 순회하고 각 연산 시간 복잡도는 O(1)이니까 O(N) 가능할듯!

import java.util.HashSet;

class Solution {
    public int[] solution(int n, String[] words) {
        // 이미 사용한 단어를 저장하는 set
        HashSet<String> usedWords = new HashSet<>();
        // 이전 단어의 마지막 글자
        char prevWord = words[0].charAt(0);

        for (int i = 0; i < words.length; i++) {
            // 이미 사용한 단어이거나 첫 글자가 이전 단어와 일치하지 않으면
            if (usedWords.contains(words[i]) || words[i].charAt(0) != prevWord) {
                // 탈락하는 사람의 번호와 차례를 반환
                return new int[]{(i % n) + 1, (i / n) + 1};
            }
            // 사용한 단어로 추가
            usedWords.add(words[i]);
            // 이전 단어의 마지막 글자 업데이트
            prevWord = words[i].charAt(words[i].length() - 1);
        }

        // 모두 통과했을 경우 반환값
        return new int[]{0, 0};
    }
}