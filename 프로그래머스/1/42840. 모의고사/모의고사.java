import java.util.ArrayList;

public class Solution {
    public int[] solution(int[] answers) {
        // 1번, 2번, 3번 수포자의 답안 패턴 정의
        int[] pattern1 = {1, 2, 3, 4, 5};
        int[] pattern2 = {2, 1, 2, 3, 2, 4, 2, 5};
        int[] pattern3 = {3, 3, 1, 1, 2, 2, 4, 4, 5, 5};

        // 맞힌 문제 개수를 저장할 배열
        int[] score = {0, 0, 0};

        // answers 배열과 비교하며 각 수포자의 맞힌 개수 계산
        for (int i = 0; i < answers.length; i++) {
            if (answers[i] == pattern1[i % pattern1.length]) {
                score[0]++;
            }
            if (answers[i] == pattern2[i % pattern2.length]) {
                score[1]++;
            }
            if (answers[i] == pattern3[i % pattern3.length]) {
                score[2]++;
            }
        }

        // 가장 높은 점수를 찾음
        int maxScore = Math.max(score[0], Math.max(score[1], score[2]));

        // 가장 높은 점수를 받은 사람을 리스트에 추가
        ArrayList<Integer> answer = new ArrayList<>();
        for (int i = 0; i < score.length; i++) {
            if (score[i] == maxScore) {
                answer.add(i + 1); // 수포자는 1번부터 시작하므로 인덱스에 +1
            }
        }

        return answer.stream().mapToInt(Integer::intValue).toArray();
    }
}