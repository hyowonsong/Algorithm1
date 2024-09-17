import java.util.Arrays;

class Solution {
    public int[] solution(int[] array, int[][] commands) {
        // 결과를 저장할 배열
        int[] answer = new int[commands.length];

        // 각 command 에 대해 처리
        for (int i = 0; i < commands.length; i++) {
            // i번째 command 를 가져옴
            int[] command = commands[i];
            int start = command[0] - 1; // 0-based index 로 변환
            int end = command[1];
            int k = command[2] - 1; // 0-based index 로 변환

            // 부분 배열을 추출
            // Arrays.copyOfRange(array, start, end)를 사용하여 start 부터 end 까지의 부분 배열을 추출
            int[] subArray = Arrays.copyOfRange(array, start, end);

            // 부분 배열을 정렬
            Arrays.sort(subArray);

            // k번째 원소를 결과 배열에 저장
            answer[i] = subArray[k];
        }

        return answer;
    }
}