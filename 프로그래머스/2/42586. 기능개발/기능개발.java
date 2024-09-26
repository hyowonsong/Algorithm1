import java.util.ArrayDeque;
import java.util.Queue;

// 기능 개발
public class Solution {
    public int[] solution(int[] progresses, int[] speeds){
        // 정답을 담을 큐를 선언
        Queue<Integer> answer = new ArrayDeque<>();

        // 작업 개수 n
        int n = progresses.length;

        // 각 작업의 남은 일수를 계산해 저장할 배열 선언
        int[] daysLeft = new int[n];
        
        // 각 작업이 완료되는 데 필요한 일수를 계산
        for (int i = 0; i < n; i++){
            // 남은 진행도(100 - progresses[i])를 속도(speeds[i])로 나눠 필요한 날짜 계산
            // Math.ceil을 통해 소수점 올림 처리 (정수형 캐스팅)
            daysLeft[i] = (int) Math.ceil((100.0 - progresses[i]) / speeds[i]);
        }

        // 현재 배포될 작업 수를 카운트하는 변수
        int count = 0;

        // 첫 번째 작업의 배포 가능일을 기준으로 설정
        int maxDay = daysLeft[0];
        
        // 각 작업의 배포 가능일을 순차적으로 확인
        for (int i = 0; i < n; i++) {
            // i번째 작업이 현재 배포 예정일보다 일찍 끝나면
            if (daysLeft[i] <= maxDay) {
                // 현재 배포될 작업 수 증가
                count++;
            }
            // i번째 작업이 더 늦게 끝날 경우
            else {
                // 현재까지 카운트된 작업 수를 큐에 추가
                answer.add(count);
                // 배포 가능한 작업 수를 1로 초기화 (새로운 작업 시작)
                count = 1;
                // 현재 작업의 배포 가능일을 가장 늦은 배포일로 업데이트
                maxDay = daysLeft[i];
            }
        }
        
        // 마지막 남은 작업 수를 큐에 추가
        answer.add(count);

        // 큐에 담긴 값을 배열로 변환해 반환
        return answer.stream().mapToInt(Integer::intValue).toArray();
    }
}