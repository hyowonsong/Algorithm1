// 피로도
public class Solution {
    // 각 던전에는 최소 필요 피로도, 소모 피로도가 존재
    // 2차원 배열 dungeons 가 매개변수로 주어짐, solution() 함수 완성

    //1. 모든 던전을 탐험 경우의 수를 보면서 최대로 탐험할 수 있는 던전 수 확인
    //2. 피로도가 있어서 도중에 탐색을 멈추가 백트래킹을 할 수 있다는 것 생각
    //2-1. 현재 피로도가 최소 필요 피로도보다 낮으면 백트레킹을 생각
    //2-2. 백트래킹은 뭔가'그래프의 가지를 치는 듯한 느낌'을 줍니다.
    //2-3. '그래프의 가지를 치는 듯한 느낌'을 pruning (분기한정)이라 합니다.
    private static int answer;
    private static int[][] Dungeons;
    private static boolean[] visited;

    public int solution(int k, int[][] dungeons) {
        answer = 0; // 탐험할 수 있는 최대 던전 수를 저장할 변수 초기화
        Dungeons = dungeons; // 주어진 던전 정보(필요 피로도와 소모 피로도)를 전역 변수에 저장

        // 던전 방문 여부를 저장할 배열, 던전의 개수만큼의 크기를 가진 boolean 배열 생성
        visited = new boolean[dungeons.length];

        backtrack(k, 0); // 백트래킹을 통해 탐험 가능한 던전 수를 계산하는 함수 호출 (현재 피로도 k, 탐험한 던전 수 0으로 시작)

        return answer; // 탐험 가능한 최대 던전 수 반환
    }

    // 백트레킹을 위한 DFS
    private static void backtrack(int k, int cnt){
        for(int i=0; i<Dungeons.length; i++){
            // 현재 피로도(k)가 i번째 던전의 최소 필요 피로도보다 크거나 같고,
            // i번째 던전을 방문한 적이 없다면
            if(k>= Dungeons[i][0] && !visited[i]){
                //i번째 던전을 방문 처리
                visited[i] = true;
                // k에서 Dungeons 소모피로도 만큼 빼주고 cnt 는 +1 해주기
                backtrack(k-Dungeons[i][1], cnt+1);
                // 2. 현재까지의 최대 탐험 가능 던전 수와
                // i 번째 던전에서 이동할 수 있는 최대 탐험 가능 던전 수 중 큰 값 선택하여 업데이트
                answer = Math.max(answer, cnt+1);
                // i번째 던전을 다시 방문 취소
                // 백트래킹의 핵심적인 과정인 상태 복원을 위해 해준다.
                // 백트레킹이 끝난 후에도 그 던전을 다시 탐험할 가능성이 있기 때문
                visited[i] = false;
            }
        }
    }
}
