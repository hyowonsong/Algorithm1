// 네트워크
// 모든 요소를 탐색하는 것이 목적이기 때문에 DFS
// 지금 n, 노드 개수를 알 수 있고 아직 탐색되지 않은 노드를 알 수 있다.
// 따라서 computers를 기준으로 그래프를 구현한 다음 번호가 낮은 노드부터
// 깊이 우선 탐색을 진행
public class Solution {
    private static boolean[] visit;
    private static int[][] computer;

    public int solution(int n, int[][] computers){
        int answer = 0;
        computer = computers;
        // 방문 여부를 저장할 배열
        visit = new boolean[n];

        for (int i = 0; i < n; i++) {
            if (!visit[i]) {
                // 아직 방문하지 않은 노드라면 해당 노드를 시작으로 깊이 우선 탐색
                dfs(i);
                answer++;
            }
        }
        return answer;
    }

    private static void dfs(int now) {
        visit[now] = true; // 현재 노드 방문 처리
        for (int i = 0; i < computer[now].length; i++) {
            // 연결되어 있으며, 방문하지 않은 노드라면
            if (computer[now][i] == 1 && !visit[i]) {
                dfs(i); // 해당 노드를 방문하러 이동
            }
        }
    }
}
