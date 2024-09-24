import java.util.HashMap;

class Solution {
    public int[] solution(int N, int[] stages) {
        // 스테이지별 도전자 수를 저장할 배열 생성 (스테이지는 1부터 시작하므로 N+2 크기로 만듦)
        int[] challenger = new int[N+2];
        // stages 배열을 순회하며 각 스테이지에 머물러 있는 도전자 수를 challenger 배열에 기록
        for (int i=0; i<stages.length; i++) {
            challenger[stages[i]] += 1;
        }

        // 스테이지별 실패율을 저장할 HashMap 생성 (Key: 스테이지 번호, Value: 실패율)
        HashMap<Integer, Double> fails = new HashMap<>();
        // 전체 도전자 수 (즉, 스테이지에 도전한 사용자 수) 저장
        double total = stages.length;

        // 각 스테이지를 순회하며, 실패율 계산
        for (int i=1; i<= N; i++){
            // 도전한 사람이 없는 경우, 실패율은 0으로 처리
            if (challenger[i] == 0) {
                fails.put(i, 0.);
            }
                // 현재 스테이지 실패율을 계산 (해당 스테이지에 도전한 사람 중 실패한 사람 비율)
            else {
                // 다음 스테이지 실패율을 구하기 위해 현재 스테이지의 도전자 수를 전체 인원에서 차감
                fails.put(i, challenger[i]/total);
                total -= challenger[i];
            }
        }

        // 실패율이 높은 스테이지부터 내림차순으로 정렬
        return fails.entrySet().stream()
                // 실패율을 기준으로 정렬 (내림차순)
                .sorted((o1, o2) -> Double.compare(o2.getValue(), o1.getValue()))
                // 정렬된 스테이지 번호를 int 배열로 변환하여 반환
                .mapToInt(HashMap.Entry::getKey)
                .toArray();
    }
}