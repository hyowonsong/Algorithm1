class Solution {
    // 연속 우승보다는 다양한 선수들이 양궁 대회에서 우승하기를 바람
    // 결승전 규칙을 전 대회 우승자인 라이언에게 불리하게

    // 어피치가 화살 n발을 다 쏜 후에 라이언이 화살 n발

    // info 의 길이 = 11
    // info 의 원소 총합 = n
    // info 의 i 번째 원소는 과녁의 10-i 점을 맞힌 화살 개수
    // 0 번째 원소는 10점이라는 뜻
    // 라이언이 우승할 방법이 있는 경우 반환할 정수 배열의 길이는 11
    // 반환할 정수 배열의 i번째 원소는 과녁의 10-i 점을 맞힌 화살 개수
    // 라이언이 가장 큰 점수 차이로 우승할 수 있는 방법이 많다면 가장 낮은 점수를 더 많이 맞힌 경우를 반환

    private static int max;
    private static int[] answer;
    private static int[] apeach;

    public static int[] solution(int n, int[] info) {
        apeach = info;
        max = 0;
        backtrack(n, 0, new int[11]);
        // 최대 차이가 0인 경우 -1 반환, 아니면 answer 반환
        if (max == 0) {
            return new int[]{-1};
        } else {
            return answer;
        }
    }

    // 주어진 조합에서 각각의 점수 계산
    private static int getScore(int[] ryan) {
        int score = 0;
        for (int i = 0; i <= 10; i++) {
            if (ryan[i] + apeach[i] > 0) {
                if (ryan[i] > apeach[i]) {
                    score += (10 - i);
                } else {
                    score -= (10 - i);
                }
            }
        }
        return score;
    }

    // 최대 차이와 라이언의 과녁 저장
    private static void calculateDiff(int[] ryan) {
        int score = getScore(ryan);
        if (max < score) {
            max = score;
            answer = ryan.clone();
        } else if (max > 0 && max == score) {
            for (int i = 10; i >= 0; i--) {
                if (answer[i] != ryan[i]) {
                    if (answer[i] < ryan[i]) {
                        answer = ryan.clone();
                    }
                    break;
                }
            }
        }
    }

    // 가능한 라이언의 과녁 점수 조합의 모든 경우를 구함
    private static void backtrack(int n, int idx, int[] ryan) {
        if (n == 0) {
            calculateDiff(ryan);
            return;
        }

        for (int i = idx; i <= 10; i++) {
            int cnt = Math.min(n, apeach[i] + 1);
            ryan[i] = cnt;
            backtrack(n - cnt, i + 1, ryan);
            ryan[i] = 0;
        }
    }
}